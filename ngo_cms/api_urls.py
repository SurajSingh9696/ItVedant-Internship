from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.api import UserViewSet
from core.api import ProgramViewSet, ProjectViewSet, BlogPostViewSet, MediaGalleryViewSet, StatisticViewSet, ContactMessageViewSet, EventViewSet
from donations.api import DonationViewSet
from volunteers.api import VolunteerViewSet, NewsletterSubscriberViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='api-users')
router.register('programs', ProgramViewSet, basename='api-programs')
router.register('projects', ProjectViewSet, basename='api-projects')
router.register('blog-posts', BlogPostViewSet, basename='api-blog-posts')
router.register('media-items', MediaGalleryViewSet, basename='api-media-items')
router.register('statistics', StatisticViewSet, basename='api-statistics')
router.register('contacts', ContactMessageViewSet, basename='api-contacts')
router.register('events', EventViewSet, basename='api-events')
router.register('donations', DonationViewSet, basename='api-donations')
router.register('volunteers', VolunteerViewSet, basename='api-volunteers')
router.register('newsletter', NewsletterSubscriberViewSet, basename='api-newsletter')

urlpatterns = [
    path('', include(router.urls)),
]
