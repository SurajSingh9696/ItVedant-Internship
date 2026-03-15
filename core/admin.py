from django.contrib import admin
from .models import Program, Project, BlogPost, MediaGallery, Statistic, ContactMessage, Event


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

