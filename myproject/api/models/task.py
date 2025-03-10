from django.db import models
from .account import Account
class Task(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Review', 'Review'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
        ('On Hold', 'On Hold'),
        ('Cancelled', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="tasks_created")
    start_date = models.DateField()
    due_date = models.DateField()
    estimated_hours = models.FloatField()
    priority = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    del_flg = models.BooleanField(default=False)  # Cờ đánh dấu xóa (0 = active, 1 = deleted)

    def soft_delete(self):
        """Đánh dấu bản ghi là đã xóa thay vì xóa vật lý"""
        self.del_flg = True
        self.save()

    def restore(self):
        """Khôi phục bản ghi đã bị đánh dấu xóa"""
        self.del_flg = False
        self.save()
        
    def __str__(self):
        return f"{self.title} ({self.status})"