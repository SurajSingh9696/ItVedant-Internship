from rest_framework import viewsets, permissions
from .models import (
    Program, Project, BlogPost, MediaGallery, Statistic, ContactMessage, Event,
    Banner, VisionMission, Initiative, Story, CoreValue, TeamMember,
    ImageGallery, VideoGallery, PressRelease, MediaCoverage, ProjectImage,
    OurStory, MediaContact
)
from .serializers import (
    ProgramSerializer, ProjectSerializer, BlogPostSerializer, MediaGallerySerializer,
    StatisticSerializer, ContactMessageSerializer, EventSerializer,
    BannerSerializer, VisionMissionSerializer, InitiativeSerializer, StorySerializer,
    CoreValueSerializer, TeamMemberSerializer, ImageGallerySerializer, VideoGallerySerializer,
    PressReleaseSerializer, MediaCoverageSerializer, ProjectImageSerializer,
    OurStorySerializer, MediaContactSerializer
)


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


class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.select_related('project').all().order_by('order', '-uploaded_at')
    serializer_class = ProjectImageSerializer
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


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all().order_by('order', '-created_at')
    serializer_class = BannerSerializer
    permission_classes = [AdminOrEditorWritePermission]


class VisionMissionViewSet(viewsets.ModelViewSet):
    queryset = VisionMission.objects.all()
    serializer_class = VisionMissionSerializer
    permission_classes = [AdminOrEditorWritePermission]


class OurStoryViewSet(viewsets.ModelViewSet):
    queryset = OurStory.objects.all().order_by('-updated_at')
    serializer_class = OurStorySerializer
    permission_classes = [AdminOrEditorWritePermission]


class InitiativeViewSet(viewsets.ModelViewSet):
    queryset = Initiative.objects.all().order_by('order', '-created_at')
    serializer_class = InitiativeSerializer
    permission_classes = [AdminOrEditorWritePermission]


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('-published_at')
    serializer_class = StorySerializer
    permission_classes = [AdminOrEditorWritePermission]


class CoreValueViewSet(viewsets.ModelViewSet):
    queryset = CoreValue.objects.all().order_by('order')
    serializer_class = CoreValueSerializer
    permission_classes = [AdminOrEditorWritePermission]


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all().order_by('order')
    serializer_class = TeamMemberSerializer
    permission_classes = [AdminOrEditorWritePermission]


class ImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = ImageGallery.objects.all().order_by('-uploaded_at')
    serializer_class = ImageGallerySerializer
    permission_classes = [AdminOrEditorWritePermission]


class VideoGalleryViewSet(viewsets.ModelViewSet):
    queryset = VideoGallery.objects.all().order_by('-uploaded_at')
    serializer_class = VideoGallerySerializer
    permission_classes = [AdminOrEditorWritePermission]


class PressReleaseViewSet(viewsets.ModelViewSet):
    queryset = PressRelease.objects.all().order_by('-published_date')
    serializer_class = PressReleaseSerializer
    permission_classes = [AdminOrEditorWritePermission]


class MediaCoverageViewSet(viewsets.ModelViewSet):
    queryset = MediaCoverage.objects.all().order_by('-published_date')
    serializer_class = MediaCoverageSerializer
    permission_classes = [AdminOrEditorWritePermission]


class MediaContactViewSet(viewsets.ModelViewSet):
    queryset = MediaContact.objects.all().order_by('-is_active', 'name')
    serializer_class = MediaContactSerializer
    permission_classes = [AdminOrEditorWritePermission]

