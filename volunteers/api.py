from rest_framework import viewsets, permissions
from .models import Volunteer, NewsletterSubscriber
from .serializers import VolunteerSerializer, NewsletterSubscriberSerializer


class VolunteerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated and request.user.role in ['admin', 'editor']
        return request.user.is_authenticated and request.user.role == 'admin'


class NewsletterPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated and request.user.role in ['admin', 'editor']
        return request.user.is_authenticated and request.user.role == 'admin'


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all().order_by('-applied_at')
    serializer_class = VolunteerSerializer
    permission_classes = [VolunteerPermission]


class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscriber.objects.all().order_by('-subscribed_at')
    serializer_class = NewsletterSubscriberSerializer
    permission_classes = [NewsletterPermission]
