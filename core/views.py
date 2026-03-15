from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Program, Project, BlogPost, MediaGallery, Statistic, ContactMessage, Event
from .forms import ContactForm


def home_view(request):
    featured_programs = Program.objects.filter(is_featured=True)[:3]
    recent_projects = Project.objects.filter(status='ongoing')[:4]
    stats = Statistic.objects.all()
    recent_blogs = BlogPost.objects.filter(is_published=True)[:3]
    context = {
        'featured_programs': featured_programs,
        'recent_projects': recent_projects,
        'stats': stats,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'core/home.html', context)


def about_view(request):
    return render(request, 'core/about.html')


def our_work_view(request):
    education = Program.objects.filter(category='education')
    healthcare = Program.objects.filter(category='healthcare')
    livelihood = Program.objects.filter(category='livelihood')
    context = {
        'education': education,
        'healthcare': healthcare,
        'livelihood': livelihood,
    }
    return render(request, 'core/our_work.html', context)


def projects_view(request):
    category = request.GET.get('category', '')
    status = request.GET.get('status', '')
    projects = Project.objects.all()
    if category:
        projects = projects.filter(category=category)
    if status:
        projects = projects.filter(status=status)
    paginator = Paginator(projects, 6)
    page = request.GET.get('page', 1)
    projects_page = paginator.get_page(page)
    return render(request, 'core/projects.html', {'projects': projects_page, 'category': category, 'status': status})


def project_detail_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})


def media_view(request):
    photos = MediaGallery.objects.filter(media_type='photo')
    videos = MediaGallery.objects.filter(media_type='video')
    press = MediaGallery.objects.filter(media_type='press')
    news = MediaGallery.objects.filter(media_type='news')
    context = {'photos': photos, 'videos': videos, 'press': press, 'news': news}
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

