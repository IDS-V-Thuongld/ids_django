from django.db import models

class Account (models.Model):
    
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True) 
    password = models.TextField
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField
    day_of_birth = models.DateField
    
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
        
    def __str__():
        return super().__str__()
    