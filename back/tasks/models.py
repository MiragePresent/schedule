from django.db import models
from datetime import datetime

class Task(models.Model):

    WAIT = 1
    DONE = 3

    STATUSES = (
        (WAIT, 'Wait'),
        (DONE, 'Done'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 300)
    day = models.DateField()
    status = models.CharField(max_length=1, choices=STATUSES, default=WAIT)

    def __str__(self):
        return self.title
