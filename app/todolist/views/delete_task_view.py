from django.contrib.auth.mixins import LoginRequiredMixin
from todolist.models import Tasks
from django.views.generic.edit import DeleteView


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Tasks
    success_url = '/'
    template_name = 'delete_confirm_page.html'