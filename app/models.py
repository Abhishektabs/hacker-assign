from django.db import models
from . views import *

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()


    def __str__(self):
        return self.name


class StatusTextChoices(models.TextChoices):
    PENDING = "Pending"
    DONE = "Done"


class Task(models.Model):
    task_detail = models.CharField(max_length=500)
    task_type = models.CharField(max_length=50,choices=StatusTextChoices.choices)
    user = models.ForeignKey(User , on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.task_detail