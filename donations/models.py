from django.db import models
import uuid


class Donation(models.Model):
    PAYMENT_TYPE = [
        ('one_time', 'One-Time'),
        ('recurring', 'Recurring'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    donor_phone = models.CharField(max_length=15, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, default='INR')
    payment_type = models.CharField(max_length=15, choices=PAYMENT_TYPE, default='one_time')
    project = models.ForeignKey('core.Project', on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(blank=True)
    razorpay_order_id = models.CharField(max_length=200, blank=True)
    razorpay_payment_id = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.donor_name} – ₹{self.amount}'

    class Meta:
        ordering = ['-created_at']

