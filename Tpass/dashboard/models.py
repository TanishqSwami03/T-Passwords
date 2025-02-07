from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.contrib.admin.models import LogEntry

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def delete(self, *args, **kwargs):
        """Delete related log entries before deleting user"""
        LogEntry.objects.filter(user_id=self.id).delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.username

class Space(models.Model):
    space_name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.space_name)

class PasswordItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    space = models.ForeignKey(Space, on_delete=models.SET_NULL, null=True)         
    password = models.CharField(max_length=100)
    created_updated = models.DateTimeField(auto_now=True)
    other_details = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['-created_updated']


    def __str__(self):
        return str(self.username)