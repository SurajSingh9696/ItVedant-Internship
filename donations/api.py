from rest_framework import viewsets, permissions
from .models import Donation
from .serializers import DonationSerializer


class DonationPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated and request.user.role in ['admin', 'editor']
        return request.user.is_authenticated and request.user.role == 'admin'


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all().order_by('-created_at')
    serializer_class = DonationSerializer
    permission_classes = [DonationPermission]

    def perform_create(self, serializer):
        serializer.save(status='pending')
