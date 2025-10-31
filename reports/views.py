from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from attendance.models import Attendance
from giving.models import Giving
from django.db.models import Count, Sum

class ReportSummaryView(APIView):
    """
    Provides summarized reports for attendance and giving.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get reports summary",
        operation_description="Returns aggregated attendance and giving statistics.",
        tags=['Reports'],
        responses={200: openapi.Response('Reports Summary')}
    )
    def get(self, request):
        attendance_total = Attendance.objects.count()
        attendance_by_type = Attendance.objects.values('event_type').annotate(total=Count('id'))
        giving_total = Giving.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        giving_by_type = Giving.objects.values('giving_type').annotate(total=Sum('amount'))

        data = {
            'attendance_summary': {
                'total': attendance_total,
                'by_type': list(attendance_by_type),
            },
            'giving_summary': {
                'total_amount': giving_total,
                'by_type': list(giving_by_type),
            },
        }
        return Response(data)
