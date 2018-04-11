from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.parsers import JSONParser
from tasks.models import TaskActivity
from tasks.serializers import TaskSerializer
from datetime import datetime

@csrf_exempt
def task_list(request):
    """
    List all code tasks, or create a new task by day
    """
    if request.method == 'GET':
        day = datetime.now().strftime("%Y-%m-%d")
        if (day in request.GET):
            day = request.GET['day']
            
        tasks = Task.objects.filter(day=day)
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, task_id):
    """
    Retrieve, update or delete a code task.
    """
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)

@csrf_exempt
def task_activity_list(request, task_id):
    """
    List all code tasks, or create a new task by day
    """
    if request.method == 'GET':
        activity = Task.objects.filter(task=task_id)
        serializer = TaskActivitySerializer(activity, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskActivitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, task_id, activity_id):
    """
    Retrieve, update or delete a code task.
    """
    try:
        activity_item = TaskActivity.objects.get(pk=activity_id, task_id=task_id)
    except TaskActivity.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskActivitySerializer(activity_item)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskActivitySerializer(activity_item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        activity_item.delete()
        return HttpResponse(status=204)
