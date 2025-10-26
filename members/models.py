from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('pastor', 'Pastor'),
        ('group_leader', 'Group Leader'),
        ('member', 'Member'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')


class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField(null=True, blank=True)
    baptism_status = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='active')
    category = models.CharField(max_length=20, default='member')

    def __str__(self):
        return f"{self.user.username} ({self.category})"
