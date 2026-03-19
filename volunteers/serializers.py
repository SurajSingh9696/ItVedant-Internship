from rest_framework import serializers
from .models import Volunteer, NewsletterSubscriber


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
        read_only_fields = ['applied_at', 'is_approved']


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = '__all__'
        read_only_fields = ['subscribed_at']
