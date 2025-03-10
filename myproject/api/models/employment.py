from django.db import models
from .group import Group
from .account import Account

class Employment(models.Model):
    position = models.CharField(max_length=255)
    start_date = models.DateField()  # Sửa lỗi từ TimeField
    end_date = models.DateField(null=True, blank=True)  # Để có thể null nếu chưa kết thúc
    qualification = models.CharField(max_length=255)
    year_exp = models.IntegerField()  # Sửa từ CharField thành IntegerField
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="employments")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="employments")
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
        return f"{self.position} - {self.account.username}"
    