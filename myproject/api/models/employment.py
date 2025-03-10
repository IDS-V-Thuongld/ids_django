from django.db import models
from .account import Account
from .department import Department

class Employment(models.Model):
    position = models.CharField(max_length=255)
    start_date = models.DateField()  # Sửa lỗi từ TimeField
    end_date = models.DateField(null=True, blank=True)  # Để có thể null nếu chưa kết thúc
    qualification = models.CharField(max_length=255)
    year_exp = models.IntegerField()  # Sửa từ CharField thành IntegerField
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employments")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="employments")
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
        return f"{self.position} - {self.account.username}"
    