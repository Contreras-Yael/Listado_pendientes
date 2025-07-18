# todo/models.py

from django.db import models

class Pendiente(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {'Resuelto' if self.completed else 'Pendiente'}"