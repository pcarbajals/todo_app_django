from django.db import models

class Task(models.Model):
    class Status(models.TextChoices):
        TO_DO = 'T'
        IN_PROGRESS = 'I'
        PENDING = 'P'
        DONE = 'D'

    title = models.CharField(max_length=120, blank=False)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.TO_DO)
    due_date = models.DateField(null=True)
    

    def _str_(self):
        return self.title
