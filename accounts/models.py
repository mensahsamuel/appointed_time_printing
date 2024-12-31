from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    department = models.CharField(max_length=50, choices=[
        ('MD', 'Managing Director'),
        ('FM', 'Finance Manager'),
        ('Sales', 'Sales'),
    ], null=True, blank=True)