from django.contrib import admin
from .models import Volunteer, NewsletterSubscriber


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'city', 'availability', 'program_interest', 'is_approved', 'applied_at')
    list_filter = ('availability', 'is_approved')
    search_fields = ('full_name', 'email', 'city', 'skills')
    list_editable = ('is_approved',)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'subscribed_at')
    list_filter = ('is_active',)

