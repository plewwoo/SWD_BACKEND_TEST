from django.db import models

# Create your models here.

class TodoList(models.Model):
    todo = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.todo