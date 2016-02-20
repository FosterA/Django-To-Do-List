from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
	taskItem = models.CharField(max_length=200)
	completionStatus = models.BooleanField(default=False)
	dueDate = models.DateTimeField()


