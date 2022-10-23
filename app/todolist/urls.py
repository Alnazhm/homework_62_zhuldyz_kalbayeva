from django.urls import path
from todolist.views.base import IndexView
from todolist.views.add_task_view import TaskAddView
from todolist.views.edit_task_view import TaskEditView
from todolist.views.delete_task_view import TaskDeleteView
from todolist.views.task_detail_view import TaskDetailView
from todolist.views.projects import ProjectDetailView,ProjectAddView,ProjectEditView,ProjectDeleteView
from todolist.views.base_project import ProjectIndexView


urlpatterns = [
    path('', ProjectIndexView.as_view(), name='index'),
    path('projects/add/', ProjectAddView.as_view(), name='add_project'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='detail_project'),
    path('projects/edit/<int:pk>', ProjectEditView.as_view(), name='edit_project'),
    path('projects/deleted/<int:pk>', ProjectDeleteView.as_view(), name='confirm_delete_project'),
    path('tasks/', IndexView.as_view(), name='index_tasks'),
    path('projects/<int:pk>/task/add/', TaskAddView.as_view(), name='task_add'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/edit/<int:pk>', TaskEditView.as_view(), name='edit_task'),
    path('tasks/deleted/<int:pk>', TaskDeleteView.as_view(), name='confirm_delete')


]