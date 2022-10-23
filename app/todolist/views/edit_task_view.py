from django.contrib.auth.mixins import LoginRequiredMixin
from todolist.models import Tasks
from django.views.generic import UpdateView
from todolist.forms import TaskForm
from django.urls import reverse


class TaskEditView(LoginRequiredMixin, UpdateView):
    template_name = 'task_edit.html'
    form_class = TaskForm
    model = Tasks
    context_object_name = 'todo_task'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


