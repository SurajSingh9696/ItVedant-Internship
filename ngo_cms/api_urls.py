from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.api import UserViewSet
from core.api import (
    ProgramViewSet, ProjectViewSet, BlogPostViewSet, MediaGalleryViewSet,
    StatisticViewSet, ContactMessageViewSet, EventViewSet,
    BannerViewSet, VisionMissionViewSet, InitiativeViewSet, StoryViewSet,
    CoreValueViewSet, TeamMemberViewSet, ImageGalleryViewSet, VideoGalleryViewSet,
    PressReleaseViewSet, MediaCoverageViewSet, ProjectImageViewSet,
    OurStoryViewSet, MediaContactViewSet
)
from donations.api import DonationViewSet
from volunteers.api import VolunteerViewSet, NewsletterSubscriberViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='api-users')
router.register('programs', ProgramViewSet, basename='api-programs')
router.register('projects', ProjectViewSet, basename='api-projects')
router.register('project-images', ProjectImageViewSet, basename='api-project-images')
router.register('blog-posts', BlogPostViewSet, basename='api-blog-posts')
router.register('media-items', MediaGalleryViewSet, basename='api-media-items')
router.register('statistics', StatisticViewSet, basename='api-statistics')
router.register('contacts', ContactMessageViewSet, basename='api-contacts')
router.register('events', EventViewSet, basename='api-events')
router.register('donations', DonationViewSet, basename='api-donations')
router.register('volunteers', VolunteerViewSet, basename='api-volunteers')
router.register('newsletter', NewsletterSubscriberViewSet, basename='api-newsletter')
router.register('banners', BannerViewSet, basename='api-banners')
router.register('vision-mission', VisionMissionViewSet, basename='api-vision-mission')
router.register('our-story', OurStoryViewSet, basename='api-our-story')
router.register('initiatives', InitiativeViewSet, basename='api-initiatives')
router.register('stories', StoryViewSet, basename='api-stories')
router.register('core-values', CoreValueViewSet, basename='api-core-values')
router.register('team-members', TeamMemberViewSet, basename='api-team-members')
router.register('image-gallery', ImageGalleryViewSet, basename='api-image-gallery')
router.register('video-gallery', VideoGalleryViewSet, basename='api-video-gallery')
router.register('press-releases', PressReleaseViewSet, basename='api-press-releases')
router.register('media-coverage', MediaCoverageViewSet, basename='api-media-coverage')
router.register('media-contacts', MediaContactViewSet, basename='api-media-contacts')

urlpatterns = [
    path('', include(router.urls)),
]
