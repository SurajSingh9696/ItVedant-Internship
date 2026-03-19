from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'role', 'status', 'is_email_verified', 'created_at']
        read_only_fields = ['id', 'is_email_verified', 'created_at']
