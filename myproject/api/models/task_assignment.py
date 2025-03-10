from django.db import models
from .employment import Employment
from .task import Task

class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="assignments")
    assignee = models.ForeignKey(Employment, on_delete=models.CASCADE, related_name="assignments")
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    progress = models.IntegerField(default=0) #Chạy từ 0 đến 100
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    is_delete = models.BooleanField(default=False)  # Cờ đánh dấu xóa (0 = active, 1 = deleted)
    
    def soft_delete(self):
        """Đánh dấu bản ghi là đã xóa thay vì xóa vật lý"""
        self.is_delete = True
        self.save()

    def restore(self):
        """Khôi phục bản ghi đã bị đánh dấu xóa"""
        self.is_delete = False
        self.save()

    def __str__(self):
        return f"{self.task.title} -> {self.assignee.username}"