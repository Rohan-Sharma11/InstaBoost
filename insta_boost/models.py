from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group
# Create your models here.

class CustomUser(AbstractUser):
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True
    )
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Change related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.'
    )




class BotRequest(models.Model):
    email_id = models.EmailField(null=False, blank=False)
    insta_profile = models.CharField(max_length=25, null=True, blank=True)
    post_url = models.CharField(max_length=100, null=True, blank=True)
    request_type_choices = [
        ('like', 'like'),
        ('comment','comment'),
        ('follow','follow'),
    ]
    request_type = models.CharField(max_length=10, choices=request_type_choices)

    date_time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('queue', 'queue'),
        ('progress', 'progress'),
        ('success', 'success'),
        ('failed', 'failed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='queue')