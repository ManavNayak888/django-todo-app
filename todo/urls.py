from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', delete_task, name='task-delete'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('task/toggle/<int:pk>/', toggle_complete, name='task-toggle'),

]
