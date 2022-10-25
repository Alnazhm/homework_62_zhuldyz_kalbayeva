from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)

@deconstructible
def first_name_val(value):
    if len(value) < 2:
        raise ValidationError('First Name is too short')
    return value


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        strip=False,
        required=True,
        widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label='Password confirmation',
        strip=False,
        required=True,
        widget=forms.PasswordInput)
    first_name = forms.CharField(
        label='First Name',
        validators=(first_name_val,),
        required=True)
    username = forms.CharField(
        label='Username',
        strip=False,
        required=True
    )
    last_name = forms.CharField(
        label='Last name',
        strip=False,
        required=True
    )
    email = forms.EmailField(
        label='Email',
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Password is not similar')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
