from django import forms
from .models import Volunteer, NewsletterSubscriber
from core.models import Program


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['full_name', 'email', 'phone', 'city', 'skills', 'availability', 'program_interest', 'motivation']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City / Location'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Teaching, Coding, Medical'}),
            'availability': forms.Select(attrs={'class': 'form-select'}),
            'program_interest': forms.Select(attrs={'class': 'form-select'}),
            'motivation': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Why do you want to volunteer?'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['program_interest'].queryset = Program.objects.all()
        self.fields['program_interest'].empty_label = 'Any Program'
        self.fields['program_interest'].required = False


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'}),
        }

