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

