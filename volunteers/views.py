from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VolunteerForm, NewsletterForm
from .models import NewsletterSubscriber


def volunteer_view(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for signing up! We will contact you shortly.')
            return redirect('get_involved')
    else:
        form = VolunteerForm()
    return render(request, 'volunteers/volunteer.html', {'form': form})


def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            obj, created = NewsletterSubscriber.objects.get_or_create(email=form.cleaned_data['email'])
            if created:
                messages.success(request, 'You have successfully subscribed to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed.')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

