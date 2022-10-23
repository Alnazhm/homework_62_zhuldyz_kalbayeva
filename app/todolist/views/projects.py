from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from todolist.models import Project, Tasks
from todolist.forms import ProjectForm


class ProjectDetailView(DetailView):
    template_name = 'detail_project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        todo_tasks = project.tasks.filter(is_deleted=False)
        context['todo_tasks'] = todo_tasks
        return context


class ProjectAddView(LoginRequiredMixin, CreateView):
    template_name = 'add_project.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})


class ProjectEditView(LoginRequiredMixin, UpdateView):
    template_name = 'edit_project.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_delete_project.html'
    model = Project
    success_url = reverse_lazy('index')
