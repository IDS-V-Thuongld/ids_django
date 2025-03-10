from django.db import models
from .department import Department
class Group(models.Model):    
    group_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="groups")
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
        return super().__str__()