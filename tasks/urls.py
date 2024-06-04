from django.urls import path
from . import views

urlpatterns = [
    path ('', views.list, name='list'),
    path('update_task/<pk>', views.updateTask, name='update_task'),
    path('delete_task/<pk>', views.deleteTask, name='delete_task'),
]