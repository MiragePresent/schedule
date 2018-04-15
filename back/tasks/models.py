from django.db import models
from datetime import datetime, date

class Task(models.Model):

    WAIT = 0
    DONE = 1

    STATUSES = (
        (WAIT, 'Wait'),
        (DONE, 'Done'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 300)
    status = models.CharField(max_length=1, choices=STATUSES, default=WAIT)
    date = models.DateField(default=date.today());
    created_at = models.DateTimeField(default=datetime.now());

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['-created_at']
