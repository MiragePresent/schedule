from django.db import models
from datetime import datetime

class Task(models.Model):

    WAIT = 1
    DONE = 2
    PARTIALLY_DONE = 3
    SKIPPED = 4

    STATUSES = (
        (WAIT, 'Wait'),
        (DONE, 'Done'),
        (PARTIALLY_DONE, 'Partially done'),
        (SKIPPED, 'Skipped'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 300)
    description = models.CharField(max_length = 1000)
    day = models.DateField()
    from_time = models.DateTimeField(default=datetime.now())
    to_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUSES, default=WAIT)
