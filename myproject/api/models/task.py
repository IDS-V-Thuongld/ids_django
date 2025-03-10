from django.db import models
from .employment import Employment
from .group import Group

class Task(models.Model):
    STATUS_CHOICES = {
        1: 'Open',
        2: 'In Progress',
        3: 'Resolved',
        4: 'Closed',
    }

    PRIORITY_CHOICES = {
        0: 'Normal',
        1: 'Priority',
    }

    ISSUE_TYPE_CHOICES = {
        1: 'Task',
        2: 'Bug',
    }
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    status = models.SmallIntegerField(choices=STATUS_CHOICES.items(), default=1)  # Lưu TinyInt
    issue_type = models.SmallIntegerField(choices=ISSUE_TYPE_CHOICES.items(), default=1)
    priority = models.SmallIntegerField(choices=PRIORITY_CHOICES.items(), default=0)

    create_user = models.CharField(max_length=255, db_column="create_user")  

    start_date = models.DateField()
    due_date = models.DateField()
    estimated_hours = models.FloatField()
    
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

    def get_status_display(self):
        """Mapping Status từ TinyInt -> Tên"""
        return self.STATUS_CHOICES.get(self.status, 'Unknown')

    def get_priority_display(self):
        """Mapping Priority từ TinyInt -> Tên"""
        return self.PRIORITY_CHOICES.get(self.priority, 'Unknown')

    def get_issue_type_display(self):
        """Mapping Issue Type từ TinyInt -> Tên"""
        return self.ISSUE_TYPE_CHOICES.get(self.issue_type, 'Unknown')

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
