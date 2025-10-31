from django.db import models
from members.models import User

class Giving(models.Model):
    GIVING_TYPE = [
        ('tithe', 'Tithe'),
        ('offering', 'Offering'),
        ('pledge', 'Pledge'),
        ('donation', 'Donation'),
    ]

    member = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    giving_type = models.CharField(max_length=20, choices=GIVING_TYPE)
    date = models.DateField(auto_now_add=True)
    method = models.CharField(max_length=50, default='Mobile Money')
    reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.member.username} - {self.giving_type} ({self.amount})"
