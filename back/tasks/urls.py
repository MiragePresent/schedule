from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list),
    path('/<int:task_id>/', views.task_detail),
]
