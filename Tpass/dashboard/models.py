from django.db import models

# Create your models here.

class Space(models.Model):
    space_name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.space_name)

class PasswordItems (models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_updated = models.DateTimeField(auto_now=True)
    other_details = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.username)