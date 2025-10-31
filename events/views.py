from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    Manage church events: creation, updates, and listings.
    """
    queryset = Event.objects.all().order_by('-start_time')
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="List all events",
        operation_description="Retrieve all church events (services, meetings, etc.)",
        tags=['Events']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create new event",
        operation_description="Add a new event with title, date, location, and type.",
        tags=['Events']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
