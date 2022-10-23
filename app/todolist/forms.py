import re
from todolist.models.statuses import Status
from todolist.models.types import Type
from todolist.models.tasks import Tasks
from django import forms
from todolist.models.projects import Project
from django.core.exceptions import ValidationError


def sum_text_validator(string):
    if '@' in string:
        raise ValidationError("You can't use @ in summary!")
    return string

def first_symbol_validator(string):
    if re.match(r'#', string):
        raise ValidationError("You can't use the first symbol # in summary!")
    return string


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    summary = forms.CharField(validators=[sum_text_validator, first_symbol_validator])

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')

class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        label='Название проекта')
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea
    )
    start_date = forms.DateField(label='Дата начала', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Дата окончания', widget=forms.SelectDateWidget)

    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),

            }



