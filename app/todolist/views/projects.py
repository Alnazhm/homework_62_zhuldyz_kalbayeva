from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView
from todolist.models import Project, Tasks
from todolist.forms import ProjectForm,AddUserToProjectForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

class GroupPermission(UserPassesTestMixin):
    groups = []
    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ProjectDetailView(DetailView):
    template_name = 'detail_project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        todo_tasks = project.tasks.filter(is_deleted=False)
        context['todo_tasks'] = todo_tasks
        return context


class ProjectAddView(GroupPermission, LoginRequiredMixin, CreateView):
    template_name = 'add_project.html'
    form_class = ProjectForm
    model = Project
    groups = ['Project Manager']

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})


class ProjectEditView(GroupPermission, LoginRequiredMixin, UpdateView):
    template_name = 'edit_project.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'
    groups = ['Project Manager']

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})


class ProjectDeleteView(GroupPermission, LoginRequiredMixin, DeleteView):
    template_name = 'confirm_delete_project.html'
    model = Project
    success_url = reverse_lazy('index')
    groups = ['Project Manager']

class AddUserToProjectView(GroupPermission, TemplateView):
    template_name = 'add_user_to_project.html'
    model = Project
    groups = ['Project Manager', 'Team Lead']

    def post(self, request, *args, **kwargs):
        self.form = AddUserToProjectForm(self.request.POST)
        if self.form.is_valid():
            users = self.form.cleaned_data.get('users')
            project = Project.objects.get(id=self.kwargs.get('pk'))
            for user in users:
                user = User.objects.get(username=user.username)
                project.users.add(user)
        return redirect('detail_project', pk=self.kwargs.get('pk'))

    def dispatch(self, request, *args, **kwargs):
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        if request.user not in project.users.all():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = AddUserToProjectForm
        return context

class ProjectUsersUpdateView(GroupPermission, LoginRequiredMixin, UpdateView):
    model = Project
    form_class = AddUserToProjectForm
    template_name = 'add_user_to_project.html'
    success_url = '/'
    groups = ['Project Manager', 'Team Lead']

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})