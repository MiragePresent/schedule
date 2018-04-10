from django.http import HttpResponse

class Task():
    """
    Tasks "controller"
    """

    def fetchOrCreate(request):
        # Get all tasks
        if (request.method == 'GET'):
            pass
        # Create new task
        if (request.method == 'POST'):
            pass

    def action(request, task_id):

        # Get a task info
        if (request.method == 'GET'):
            pass

        # Update a tast
        if (request.method == 'PUT' or request.method == 'PATCH'):
            pass
            
        # Delete a task
        if (request.method == 'DELETE'):
            pass
