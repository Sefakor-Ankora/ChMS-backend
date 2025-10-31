from django.urls import path
from .views import ReportSummaryView

urlpatterns = [
    path('reports/', ReportSummaryView.as_view(), name='reports-summary'),
]
