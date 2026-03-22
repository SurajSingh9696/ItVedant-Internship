from django.db import models
from django.utils.text import slugify


class Program(models.Model):
    CATEGORY_CHOICES = [
        ('education', 'Education'),
        ('healthcare', 'Healthcare'),
        ('livelihood', 'Livelihood'),
        ('women', 'Women Empowerment'),
        ('environment', 'Environment'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.TextField()
    impact_count = models.PositiveIntegerField(default=0, help_text='Number of beneficiaries')
    image = models.ImageField(upload_to='programs/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Project(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=30, choices=Program.CATEGORY_CHOICES)
    description = models.TextField()
    goals = models.TextField(blank=True)
    beneficiaries = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    report = models.FileField(upload_to='reports/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_gallery/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.project.title} image'

    class Meta:
        ordering = ['order', '-uploaded_at']


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at', '-created_at']


class MediaGallery(models.Model):
    TYPE_CHOICES = [
        ('photo', 'Photo'),
        ('video', 'Video'),
        ('press', 'Press Release'),
        ('news', 'News Coverage'),
    ]
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='photo')
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    video_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']
        verbose_name_plural = 'Media Gallery'


class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, blank=True, help_text='Bootstrap icon class')
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.label}: {self.value}'

    class Meta:
        ordering = ['order']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} – {self.subject}'

    class Meta:
        ordering = ['-submitted_at']


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['event_date']


class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='banners/')
    cta_text = models.CharField(max_length=50, blank=True)
    cta_link = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', '-created_at']


class VisionMission(models.Model):
    vision_title = models.CharField(max_length=200, default='Our Vision')
    vision_text = models.TextField()
    mission_title = models.CharField(max_length=200, default='Our Mission')
    mission_text = models.TextField()
    values_intro = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Vision & Mission'

    class Meta:
        verbose_name = 'Vision & Mission'
        verbose_name_plural = 'Vision & Mission'


class OurStory(models.Model):
    title = models.CharField(max_length=200, default='Our Story')
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    milestones = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Our Story'
        verbose_name_plural = 'Our Story'


class Initiative(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='initiatives/', blank=True, null=True)
    impact_text = models.CharField(max_length=200, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', '-created_at']


class Story(models.Model):
    CATEGORY_CHOICES = [
        ('education', 'Education'),
        ('healthcare', 'Healthcare'),
        ('livelihood', 'Livelihood'),
        ('women', 'Women Empowerment'),
        ('community', 'Community Development'),
    ]
    title = models.CharField(max_length=200)
    beneficiary_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)
    story_text = models.TextField()
    quote = models.TextField(blank=True)
    image = models.ImageField(upload_to='stories/', blank=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='community')
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.beneficiary_name} - {self.title}'

    class Meta:
        ordering = ['-published_at']
        verbose_name_plural = 'Stories'


class CoreValue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.designation}'

    class Meta:
        ordering = ['order']


class ImageGallery(models.Model):
    CATEGORY_CHOICES = [
        ('event', 'Event'),
        ('program', 'Program'),
        ('project', 'Project'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image_gallery/')
    caption = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name_plural = 'Image Gallery'


class VideoGallery(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='video_gallery/', blank=True, null=True)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=20, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name_plural = 'Video Gallery'


class PressRelease(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pdf_file = models.FileField(upload_to='press_releases/', blank=True, null=True)
    published_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']


class MediaCoverage(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('news', 'News Article'),
        ('tv', 'TV Coverage'),
        ('radio', 'Radio'),
        ('online', 'Online Media'),
    ]
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='media_coverage/', blank=True, null=True)
    description = models.TextField(blank=True)
    published_date = models.DateField()
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPE_CHOICES, default='news')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {self.source}'

    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'Media Coverage'


class MediaContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-is_active', 'name']

