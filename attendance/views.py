# attendance/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing member attendance records.

    list:
    Retrieve all attendance records.

    create:
    Record new attendance for a member.

    retrieve:
    View details for a single attendance record.

    update:
    Edit an existing attendance entry.

    delete:
    Remove an attendance record.
    """
    queryset = Attendance.objects.all().order_by('-date')
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="List attendance records",
        operation_description="Retrieve all attendance records for church services, groups, or events.",
        tags=['Attendance'],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create attendance record",
        operation_description="Record new attendance for a member with event type and remarks.",
        tags=['Attendance'],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
