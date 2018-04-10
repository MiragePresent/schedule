from django.urls import path
from . import rest

urlpatterns = [
    path('', rest.Task.fetchOrCreate),
    path('/<int:taks_id>', rest.Task.action)
]
