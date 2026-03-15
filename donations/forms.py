from django import forms
from .models import Donation
from core.models import Project


class DonationForm(forms.ModelForm):
    AMOUNT_CHOICES = [
        (500, '₹500'),
        (1000, '₹1,000'),
        (2500, '₹2,500'),
        (5000, '₹5,000'),
        (10000, '₹10,000'),
        (0, 'Custom Amount'),
    ]

    preset_amount = forms.ChoiceField(
        choices=AMOUNT_CHOICES,
        required=False,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Choose Amount'
    )

    class Meta:
        model = Donation
        fields = ['donor_name', 'donor_email', 'donor_phone', 'amount', 'payment_type', 'project', 'message']
        widgets = {
            'donor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'donor_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'donor_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number (optional)'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount in INR', 'min': '10'}),
            'payment_type': forms.Select(attrs={'class': 'form-select'}),
            'project': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Leave a message (optional)'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.all()
        self.fields['project'].empty_label = 'General Fund (Any Program)'
        self.fields['project'].required = False
        self.fields['amount'].required = True

