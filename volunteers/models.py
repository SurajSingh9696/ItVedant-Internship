from django.db import models


class Volunteer(models.Model):
    AVAILABILITY = [
        ('weekdays', 'Weekdays'),
        ('weekends', 'Weekends'),
        ('both', 'Both'),
        ('remote', 'Remote Only'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)
    skills = models.TextField(blank=True, help_text='Comma-separated skills')
    availability = models.CharField(max_length=15, choices=AVAILABILITY, default='weekends')
    motivation = models.TextField(blank=True)
    program_interest = models.ForeignKey(
        'core.Program', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='volunteers'
    )
    applied_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        ordering = ['-applied_at']


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-subscribed_at']

