from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberProfileViewSet

router = DefaultRouter()
router.register(r'members', MemberProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
