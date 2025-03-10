from django.db import models
from .account import Account
from .task import Task

class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="assignments")
    assignee = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="assignments")
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    progress = models.IntegerField(default=0) #Chạy từ 0 đến 100
    def __str__(self):
        return f"{self.task.title} -> {self.assignee.username}"