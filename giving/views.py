# giving/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import Giving
from .serializers import GivingSerializer

class GivingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for recording member giving (tithes, offerings, pledges, donations).

    list:
    Retrieve all giving records.

    create:
    Add a new giving record for a member.

    retrieve:
    Get details of a specific giving record.

    update:
    Update a giving entry.

    delete:
    Remove a giving record.
    """
    queryset = Giving.objects.all().order_by('-date')
    serializer_class = GivingSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="List giving records",
        operation_description="Retrieve all giving entries including tithes, offerings, and donations.",
        tags=['Giving'],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Record giving entry",
        operation_description="Record a new giving entry with amount, type, and payment method.",
        tags=['Giving'],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
