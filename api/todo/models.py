from django.db import models

class Task(models.Model):
    ''' The Task model has four fields: title, description, status and due date '''
    class Status(models.TextChoices):
        TO_DO = 'T'
        IN_PROGRESS = 'I'
        PENDING = 'P'
        DONE = 'D'

    title = models.CharField(max_length=120, blank=False)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.TO_DO)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.title
