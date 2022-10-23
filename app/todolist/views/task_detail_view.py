from todolist.models import Tasks
from django.views.generic import DetailView


class TaskDetailView(DetailView):
    template_name = 'task.html'
    model = Tasks
    context_object_name = 'todo_task'

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        return queryset