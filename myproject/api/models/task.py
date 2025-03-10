from django.db import models
from .employment import Employment
from .group import Group

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

    create_user = models.CharField(max_length=255, db_column="create_user")  

    start_date = models.DateField()
    due_date = models.DateField()
    estimated_hours = models.FloatField()
    priority = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    assigned_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    is_delete = models.BooleanField(default=False)  

    def soft_delete(self):
        """Đánh dấu bản ghi là đã xóa thay vì xóa vật lý"""
        self.is_delete = True
        self.save()

    def restore(self):
        """Khôi phục bản ghi đã bị đánh dấu xóa"""
        self.is_delete = False
        self.save()
        
    def __str__(self):
        return f"{self.title} ({self.status})"
