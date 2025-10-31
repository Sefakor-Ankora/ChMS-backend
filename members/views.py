from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import MemberProfile
from .serializers import MemberProfileSerializer

class MemberProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing church members.
    
    retrieve:
    Get details of a specific member.
    
    list:
    Get a list of all members.
    
    create:
    Add a new member and user record.
    
    update:
    Update member details.
    
    delete:
    Delete a member record.
    """

    queryset = MemberProfile.objects.select_related('user').all()
    serializer_class = MemberProfileSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="List all members",
        operation_description="Retrieve a list of all church members with associated user details.",
        tags=['Members'],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new member",
        operation_description="Register a new church member along with user credentials.",
        tags=['Members'],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializer, UserSerializer, MemberProfileSerializer
from .models import User, MemberProfile

class RegisterView(generics.CreateAPIView):
    """User registration endpoint."""
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer  # ✅ Added for Swagger

    @swagger_auto_schema(
        operation_summary="Register a new member",
        operation_description="Register a new church member with associated user and profile data.",
        tags=["Auth"],
        responses={
            201: "User registered successfully",
            400: "Invalid input data"
        }
    )
    def post(self, request, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # Avoid running DB code during schema generation
            return None

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
