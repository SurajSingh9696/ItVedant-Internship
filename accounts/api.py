from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer


class AdminOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [AdminOnlyPermission]
