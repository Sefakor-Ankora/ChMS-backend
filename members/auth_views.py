# members/auth_views.py
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Request body schemas for swagger
token_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
    },
    required=['username', 'password']
)

refresh_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token'),
    },
    required=['refresh']
)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Obtain JWT access and refresh tokens.

    Request example:
    {
      "username": "admin",
      "password": "yourpassword"
    }

    Response example:
    {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    """

    @swagger_auto_schema(
        operation_summary="Login and obtain JWT tokens",
        request_body=token_request_schema,
        responses={200: openapi.Response('Tokens', schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING),
                'access': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ))},
        tags=['Auth'],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    """
    Refresh an access token using a refresh token.

    Request example:
    {
      "refresh": "<refresh_token>"
    }

    Response example:
    {
      "access": "<new_access_token>"
    }
    """

    @swagger_auto_schema(
        operation_summary="Refresh access token",
        request_body=refresh_request_schema,
        responses={200: openapi.Response('New access token', schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'access': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ))},
        tags=['Auth'],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
