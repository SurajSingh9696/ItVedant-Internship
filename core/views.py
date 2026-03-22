from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.utils import OperationalError, ProgrammingError
from .models import (
    Program, Project, BlogPost, MediaGallery, Statistic, ContactMessage, Event,
    Banner, VisionMission, Initiative, Story, CoreValue, TeamMember,
    ImageGallery, VideoGallery, PressRelease, MediaCoverage, OurStory, MediaContact
)
from .forms import ContactForm


def _safe_list(queryset):
    try:
        return list(queryset)
    except (ProgrammingError, OperationalError):
        return []


def _safe_first(queryset):
    try:
        return queryset.first()
    except (ProgrammingError, OperationalError):
        return None


def home_view(request):
    banners = _safe_list(Banner.objects.filter(is_active=True).order_by('order'))
    featured_programs = _safe_list(Program.objects.filter(is_featured=True)[:3])
    recent_projects = _safe_list(Project.objects.filter(status='ongoing')[:4])
    stats = _safe_list(Statistic.objects.all())
    recent_blogs = _safe_list(BlogPost.objects.filter(is_published=True)[:3])
    featured_initiatives = _safe_list(Initiative.objects.filter(is_featured=True).order_by('order')[:3])
    featured_stories = _safe_list(Story.objects.filter(is_featured=True).order_by('-published_at')[:2])
    vision_mission = _safe_first(VisionMission.objects.all())
    context = {
        'banners': banners,
        'featured_programs': featured_programs,
        'recent_projects': recent_projects,
        'stats': stats,
        'recent_blogs': recent_blogs,
        'featured_initiatives': featured_initiatives,
        'featured_stories': featured_stories,
        'vision_mission': vision_mission,
    }
    return render(request, 'core/home.html', context)


def about_view(request):
    vision_mission = _safe_first(VisionMission.objects.all())
    our_story = _safe_first(OurStory.objects.all())
    core_values = _safe_list(CoreValue.objects.all().order_by('order'))
    team_members = _safe_list(TeamMember.objects.filter(is_active=True).order_by('order'))
    programs = _safe_list(Program.objects.all().order_by('-created_at')[:6])
    stats = _safe_list(Statistic.objects.all().order_by('order')[:4])
    featured_stories = _safe_list(Story.objects.filter(is_featured=True).order_by('-published_at')[:3])
    context = {
        'vision_mission': vision_mission,
        'our_story': our_story,
        'core_values': core_values,
        'team_members': team_members,
        'programs': programs,
        'stats': stats,
        'featured_stories': featured_stories,
    }
    return render(request, 'core/about.html', context)


def our_work_view(request):
    education = _safe_list(Program.objects.filter(category='education'))
    healthcare = _safe_list(Program.objects.filter(category='healthcare'))
    livelihood = _safe_list(Program.objects.filter(category='livelihood'))
    context = {
        'education': education,
        'healthcare': healthcare,
        'livelihood': livelihood,
    }
    return render(request, 'core/our_work.html', context)


def projects_view(request):
    category = request.GET.get('category', '')
    status = request.GET.get('status', '')
    q = request.GET.get('q', '')
    projects = Project.objects.all()
    if category:
        projects = projects.filter(category=category)
    if status:
        projects = projects.filter(status=status)
    if q:
        projects = projects.filter(title__icontains=q)
    paginator = Paginator(projects, 6)
    page = request.GET.get('page', 1)
    projects_page = paginator.get_page(page)
    return render(
        request,
        'core/projects.html',
        {'projects': projects_page, 'category': category, 'status': status, 'q': q},
    )


def project_detail_view(request, slug):
    project = get_object_or_404(Project.objects.prefetch_related('images'), slug=slug)
    related_projects = Project.objects.filter(category=project.category).exclude(pk=project.pk)[:3]
    return render(
        request,
        'core/project_detail.html',
        {
            'project': project,
            'project_images': project.images.all(),
            'related_projects': related_projects,
        },
    )


def media_view(request):
    images = _safe_list(ImageGallery.objects.all().order_by('-uploaded_at'))
    videos = _safe_list(VideoGallery.objects.all().order_by('-uploaded_at'))
    press_releases = _safe_list(PressRelease.objects.all().order_by('-published_date'))
    media_coverage = _safe_list(MediaCoverage.objects.all().order_by('-published_date'))
    media_contacts = _safe_list(MediaContact.objects.filter(is_active=True).order_by('name'))
    context = {
        'images': images,
        'videos': videos,
        'press_releases': press_releases,
        'media_coverage': media_coverage,
        'media_contacts': media_contacts,
    }
    return render(request, 'core/media.html', context)


def get_involved_view(request):
    events = Event.objects.all()[:6]
    return render(request, 'core/get_involved.html', {'events': events})


def blog_view(request):
    posts = BlogPost.objects.filter(is_published=True)
    paginator = Paginator(posts, 6)
    page = request.GET.get('page', 1)
    posts_page = paginator.get_page(page)
    return render(request, 'core/blog.html', {'posts': posts_page})


def blog_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    recent = BlogPost.objects.filter(is_published=True).exclude(slug=slug)[:3]
    return render(request, 'core/blog_detail.html', {'post': post, 'recent': recent})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. We will get back to you soon!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

