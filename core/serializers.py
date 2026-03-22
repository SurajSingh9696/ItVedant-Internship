from rest_framework import serializers
from .models import (
    Program, Project, BlogPost, MediaGallery, Statistic, ContactMessage, Event,
    Banner, VisionMission, Initiative, Story, CoreValue, TeamMember,
    ImageGallery, VideoGallery, PressRelease, MediaCoverage, ProjectImage,
    OurStory, MediaContact
)


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'
        read_only_fields = ['uploaded_at']


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class MediaGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaGallery
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        read_only_fields = ['created_at']


class VisionMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisionMission
        fields = '__all__'
        read_only_fields = ['updated_at']


class OurStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurStory
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class InitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Initiative
        fields = '__all__'
        read_only_fields = ['created_at']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'
        read_only_fields = ['published_at']


class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = '__all__'
        read_only_fields = ['created_at']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = '__all__'
        read_only_fields = ['uploaded_at']


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = '__all__'
        read_only_fields = ['uploaded_at']


class PressReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressRelease
        fields = '__all__'
        read_only_fields = ['created_at']


class MediaCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaCoverage
        fields = '__all__'


class MediaContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaContact
        fields = '__all__'
        read_only_fields = ['updated_at']

