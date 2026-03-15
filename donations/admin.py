from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'donor_email', 'amount', 'currency', 'payment_type', 'status', 'created_at')
    list_filter = ('status', 'payment_type', 'currency')
    search_fields = ('donor_name', 'donor_email', 'transaction_id')
    readonly_fields = ('transaction_id', 'created_at', 'razorpay_order_id', 'razorpay_payment_id')

