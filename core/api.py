from rest_framework import viewsets, permissions
from .models import Program, Project, BlogPost, MediaGallery, Statistic, ContactMessage, Event
from .serializers import ProgramSerializer, ProjectSerializer, BlogPostSerializer, MediaGallerySerializer, StatisticSerializer, ContactMessageSerializer, EventSerializer


class AdminOrEditorWritePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role in ['admin', 'editor']


class ContactMessagePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated and request.user.role in ['admin', 'editor']
        return request.user.is_authenticated and request.user.role == 'admin'


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all().order_by('-created_at')
    serializer_class = ProgramSerializer
    permission_classes = [AdminOrEditorWritePermission]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [AdminOrEditorWritePermission]


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    permission_classes = [AdminOrEditorWritePermission]


class MediaGalleryViewSet(viewsets.ModelViewSet):
    queryset = MediaGallery.objects.all().order_by('-published_at')
    serializer_class = MediaGallerySerializer
    permission_classes = [AdminOrEditorWritePermission]


class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all().order_by('order')
    serializer_class = StatisticSerializer
    permission_classes = [AdminOrEditorWritePermission]


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-submitted_at')
    serializer_class = ContactMessageSerializer
    permission_classes = [ContactMessagePermission]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('event_date')
    serializer_class = EventSerializer
    permission_classes = [AdminOrEditorWritePermission]
