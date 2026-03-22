from django.contrib import admin
from .models import (
    Program, Project, BlogPost, MediaGallery, Statistic, ContactMessage, Event,
    Banner, VisionMission, Initiative, Story, CoreValue, TeamMember,
    ImageGallery, VideoGallery, PressRelease, MediaCoverage, ProjectImage,
    OurStory, MediaContact
)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'impact_count', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'beneficiaries', 'location', 'created_at')
    list_filter = ('category', 'status')
    search_fields = ('title', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'order', 'uploaded_at')
    list_filter = ('project',)
    search_fields = ('project__title', 'caption')
    list_editable = ('order',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'published_at', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(MediaGallery)
class MediaGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'published_at')
    list_filter = ('media_type',)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'subject')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'location')
    search_fields = ('title', 'location')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    list_editable = ('order', 'is_active')


@admin.register(VisionMission)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ('vision_title', 'mission_title', 'updated_at')

    def has_add_permission(self, request):
        return not VisionMission.objects.exists()


@admin.register(OurStory)
class OurStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'founded_year', 'updated_at')

    def has_add_permission(self, request):
        return not OurStory.objects.exists()


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_featured', 'created_at')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_featured')


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('beneficiary_name', 'title', 'category', 'location', 'is_featured', 'published_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('beneficiary_name', 'title', 'location')
    list_editable = ('is_featured',)


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('order',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'is_active', 'order', 'joined_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'designation', 'email')
    list_editable = ('order', 'is_active')


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'uploaded_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'caption')
    list_editable = ('is_featured',)


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'is_featured', 'uploaded_at')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')
    list_editable = ('is_featured',)


@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'published_date')
    search_fields = ('title', 'content')
    list_editable = ('is_featured',)


@admin.register(MediaCoverage)
class MediaCoverageAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'media_type', 'published_date', 'is_featured')
    list_filter = ('media_type', 'is_featured', 'published_date')
    search_fields = ('title', 'source', 'description')
    list_editable = ('is_featured',)


@admin.register(MediaContact)
class MediaContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'email', 'phone', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'designation', 'email', 'phone')
    list_editable = ('is_active',)
