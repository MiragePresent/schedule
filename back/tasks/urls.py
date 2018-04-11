from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list),
    path('/<int:task_id>/', views.task_detail),
    path('/<int:task_id>/activity/', views.task_activity_list),
    path('/<int:task_id>/activity/<int:acvitity_id>', views.task_activity_list),
]
