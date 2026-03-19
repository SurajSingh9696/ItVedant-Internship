from rest_framework import serializers
from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
        read_only_fields = ['transaction_id', 'status', 'razorpay_order_id', 'razorpay_payment_id', 'created_at']
