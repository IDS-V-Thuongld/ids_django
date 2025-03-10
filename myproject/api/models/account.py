from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class AccountManager(BaseUserManager):
    """Quản lý user"""
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Hash password trước khi lưu
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """Tạo superuser"""
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True) 
    password = models.CharField(max_length=255)  # Django sẽ tự hash password
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    day_of_birth = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    is_active = models.BooleanField(default=True)  # Tài khoản có thể đăng nhập không?
    is_admin = models.BooleanField(default=False)  # Có quyền admin không?
    is_delete = models.BooleanField(default=False)  # Đánh dấu đã xóa (Soft delete)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="account_users",  # Đổi tên tránh trùng với `auth.User`
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="account_users_permissions",  # Đổi tên tránh trùng với `auth.User`
        blank=True
    )

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        """Cần có để Django Admin nhận diện user có quyền admin"""
        return self.is_admin
