from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ('service', 'Service'),
        ('meeting', 'Meeting'),
        ('outreach', 'Outreach'),
        ('conference', 'Conference'),
        ('wedding', 'Wedding'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.event_type}"
