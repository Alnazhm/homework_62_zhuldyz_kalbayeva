from django.contrib.auth.mixins import LoginRequiredMixin
from todolist.models import Tasks
from django.views.generic import CreateView
from todolist.forms import TaskForm
from django.urls import reverse


class TaskAddView(LoginRequiredMixin, CreateView):
    template_name = 'create_task.html'
    form_class = TaskForm
    model = Tasks

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        return super(TaskAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})