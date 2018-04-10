from django.db import models

class Task(models.Models):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_lenght = 300)
    description = models.CharField(max_length = 1000)
    day = models.DateField()
    to_time = models.DateTimeField()
    to_time = models.DateTimeField()
