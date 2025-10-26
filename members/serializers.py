from rest_framework import serializers
from .models import User, MemberProfile

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user data with role-based information."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']
        extra_kwargs = {
            'username': {'help_text': 'Unique username for login.'},
            'email': {'help_text': 'User email address.'},
            'role': {'help_text': 'Role of the user (admin, pastor, group_leader, member).'}
        }

class MemberProfileSerializer(serializers.ModelSerializer):
    """Serializer for church member profiles."""
    
    user = UserSerializer(help_text="User object linked to this member profile.")

    class Meta:
        model = MemberProfile
        fields = '__all__'
        extra_kwargs = {
            'birthday': {'help_text': 'Date of birth of the member (YYYY-MM-DD).'},
            'baptism_status': {'help_text': 'Boolean flag indicating baptism status.'},
            'status': {'help_text': 'Active, inactive, or transferred.'},
            'category': {'help_text': 'Member category (visitor, member, staff, volunteer).'},
        }
