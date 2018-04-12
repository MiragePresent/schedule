from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
