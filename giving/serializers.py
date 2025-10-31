from rest_framework import serializers
from .models import Giving

class GivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Giving
        fields = '__all__'
