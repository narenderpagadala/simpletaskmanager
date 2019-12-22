from django.db import models


# Create your models here.
class Task_Models(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.TextField(max_length=150)
    task_assign_date = models.DateField(default=None)
    task_complete_date = models.DateField()
    assigning_to = models.CharField(max_length=50)
    priority = models.CharField(max_length=50, default=None)

class Task_Models_Post(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.TextField(max_length=150)
    task_assign_date = models.DateField(default=None)
    task_complete_date = models.DateField()
    assigning_to = models.CharField(max_length=50)
    priority = models.CharField(max_length=50, default=None)
    status = models.CharField(max_length=50, default=None)
