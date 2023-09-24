from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
