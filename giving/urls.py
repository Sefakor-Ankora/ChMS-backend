from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GivingViewSet

router = DefaultRouter()
router.register(r'giving', GivingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
