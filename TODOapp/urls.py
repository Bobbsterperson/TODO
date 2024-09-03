from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, toggle_task_completion

urlpatterns = [
    path('', TaskList.as_view(), name='TODOs'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task_confirm_delete'),
    path('task-toggle/<int:pk>/', toggle_task_completion, name='task-toggle'),
]
