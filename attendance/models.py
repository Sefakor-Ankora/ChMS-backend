from django.db import models
from members.models import User

class Attendance(models.Model):
    EVENT_TYPE = [
        ('service', 'Service'),
        ('group', 'Group Meeting'),
        ('event', 'Event'),
    ]

    member = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.username} - {self.event_type} ({self.date})"
