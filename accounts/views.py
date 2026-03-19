from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm, LoginForm, CustomPasswordResetForm, CustomSetPasswordForm

User = get_user_model()


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_email_verified = False
            user.is_active = False
            user.save(update_fields=['is_email_verified', 'is_active'])
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            verify_link = request.build_absolute_uri(reverse('verify_email', args=[uid, token]))
            send_mail(
                'Verify your email - HopeForward NGO',
                f'Hi {user.full_name},\n\nPlease verify your email to activate your account:\n{verify_link}\n\nIf you did not register, please ignore this message.',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=True,
            )
            messages.success(request, 'Account created. Please verify your email before login.')
            return redirect('verify_email_sent')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_email_verified and user.role != 'admin':
                messages.error(request, 'Please verify your email before logging in.')
                return redirect('login')
            if user.role == 'admin' and (not user.is_staff or not user.is_superuser):
                user.is_staff = True
                user.is_superuser = True
                user.save(update_fields=['is_staff', 'is_superuser'])
            login(request, user)
            messages.success(request, f'Welcome back, {user.full_name}!')
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


@login_required
def dashboard_view(request):
    from core.models import BlogPost, Project, Program
    from donations.models import Donation
    from volunteers.models import Volunteer
    stats = {
        'total_users': User.objects.count(),
        'total_donations': Donation.objects.count(),
        'total_volunteers': Volunteer.objects.count(),
        'total_projects': Project.objects.count(),
        'total_blogs': BlogPost.objects.count(),
        'recent_donations': Donation.objects.order_by('-created_at')[:5],
        'recent_volunteers': Volunteer.objects.order_by('-applied_at')[:5],
    }
    return render(request, 'accounts/dashboard.html', stats)


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def manage_users_view(request):
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard')
    users = User.objects.all().order_by('-created_at')
    return render(request, 'accounts/manage_users.html', {'users': users})


@login_required
def toggle_user_status(request, pk):
    if request.user.role != 'admin':
        messages.error(request, 'Access denied.')
        return redirect('dashboard')
    user = User.objects.get(pk=pk)
    if user == request.user:
        messages.error(request, 'You cannot change your own status.')
        return redirect('manage_users')
    if user.role == 'admin':
        messages.error(request, 'Admin users cannot be deactivated.')
        return redirect('manage_users')
    user.status = 'inactive' if user.status == 'active' else 'active'
    user.is_active = user.status == 'active'
    user.save()
    messages.success(request, f'User status updated.')
    return redirect('manage_users')


def verify_email_sent_view(request):
    return render(request, 'accounts/verify_email_sent.html')


def verify_email_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_email_verified = True
        user.is_active = True
        user.save(update_fields=['is_email_verified', 'is_active'])
        return render(request, 'accounts/verify_email_result.html', {'verified': True})

    return render(request, 'accounts/verify_email_result.html', {'verified': False})


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'accounts/forgot_password.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'accounts/reset_password.html'
    success_url = reverse_lazy('login')

