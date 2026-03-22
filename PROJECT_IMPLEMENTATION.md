# HopeForward NGO Site: Project Implementation Guide

## Overview
This project is a Django-based NGO CMS. It provides dynamic website pages and backend/admin content management for Home, About Us, Our Work, Projects, Media, Blog, Contact, Donations, and Volunteers.

The implementation is split across apps:
- `accounts`: authentication, roles, profile, user management
- `core`: CMS content models, page rendering, APIs for site content
- `donations`: donation flow and payment handling
- `volunteers`: volunteer form and newsletter subscriptions
- `ngo_cms`: project settings, URL routing, API root routing

## PDF Alignment Summary
The attached PDF requirements were implemented by ensuring:
- Home page has backend-managed banner slider, vision/mission, statistics, initiatives, projects, and impact content.
- About Us page has backend-managed Our Story, Vision/Mission, Core Values, Programs, Team, and impact sections.
- Projects page supports status/category filtering and project detail pages with more context and gallery.
- Media page supports image gallery, videos, press releases, media coverage, and media contact details.
- Admin dashboard controls all content through Django admin with authenticated access.

## Data Model Implementation (`core/models.py`)
### Existing primary content models
- `Program`
- `Project`
- `BlogPost`
- `Statistic`
- `ContactMessage`
- `Event`
- `Banner`
- `VisionMission`
- `Initiative`
- `Story`
- `CoreValue`
- `TeamMember`
- `ImageGallery`
- `VideoGallery`
- `PressRelease`
- `MediaCoverage`

### Added/extended for PDF-complete behavior
- `ProjectImage`
  - Foreign key to `Project`
  - Multiple images per project detail page
  - Ordered gallery support
- `OurStory`
  - Title, long-form story content, optional image, founded year, milestones
  - Used for dynamic About Us “Our Story” section
- `MediaContact`
  - Name, email, phone, designation, active status
  - Used for media inquiries section on Media page

## Migrations
A migration was generated and applied:
- `core/migrations/0002_banner_corevalue_imagegallery_initiative_and_more.py`

Migration state verified with:
- `python manage.py makemigrations --check --dry-run`
- `python manage.py showmigrations core`
- `python manage.py migrate`

## Admin CMS (`core/admin.py`)
All key content models are registered in admin and configured for practical content operations.

Added admin management for:
- `ProjectImage`
- `OurStory`
- `MediaContact`

This allows the admin to manage Home/About/Projects/Media sections directly from Django admin.

## API Layer
### Serializers (`core/serializers.py`)
Added serializers for:
- `ProjectImageSerializer`
- `OurStorySerializer`
- `MediaContactSerializer`

### ViewSets (`core/api.py`)
Added ViewSets for:
- `ProjectImageViewSet`
- `OurStoryViewSet`
- `MediaContactViewSet`

Existing role-based write permissions remain in effect.

### API Routes (`ngo_cms/api_urls.py`)
Added API endpoints:
- `/api/project-images/`
- `/api/our-story/`
- `/api/media-contacts/`

## Frontend Page Implementation
### Home page (`templates/core/home.html`)
Implemented dynamic content blocks:
- banner slider from `Banner`
- vision/mission from `VisionMission`
- statistics from `Statistic`
- initiatives from `Initiative`
- featured projects from `Project`
- success stories from `Story`

### About Us page (`templates/core/about.html`)
Implemented dynamic sections:
- Our Story from `OurStory`
- Vision and Mission from `VisionMission`
- Core Values from `CoreValue`
- Focus Programs from `Program`
- Team Members from `TeamMember`
- Impact blocks from `Statistic` and featured stories

### Projects list page (`templates/core/projects.html`)
Implemented:
- search by title (`q`)
- filter by category
- filter by status (Ongoing, Completed, Upcoming)
- pagination preserved

### Project detail page (`templates/core/project_detail.html`)
Implemented:
- full project details
- gallery from related `ProjectImage`
- related projects by category
- support CTA

### Media page (`templates/core/media.html`)
Fixed data mismatches and implemented:
- Image Gallery from `ImageGallery`
- Videos from `VideoGallery`
- Press Releases from `PressRelease`
- Media Coverage from `MediaCoverage`
- Media Contacts from `MediaContact`

## View Logic Updates (`core/views.py`)
Updated context wiring for correctness and dynamic rendering:
- `home_view`: includes `vision_mission`
- `about_view`: includes `our_story`, stats, featured stories
- `projects_view`: supports `q` search with category/status filtering
- `project_detail_view`: prefetches project images and related projects
- `media_view`: provides `images`, `videos`, `press_releases`, `media_coverage`, `media_contacts`

## Validation and Health Checks
Commands run:
- `python manage.py check`
- `python manage.py test`
- `python manage.py makemigrations --check --dry-run`
- `python manage.py showmigrations core`
- `python manage.py migrate`

Result:
- No pending migrations
- System checks passed
- No test failures (repository currently has no tests)

## How to Manage Content (Admin Workflow)
1. Login to Django admin as admin/editor-enabled user.
2. Update Home sections via: `Banners`, `Vision & Mission`, `Statistic`, `Initiative`, `Story`.
3. Update About Us via: `Our Story`, `Core Value`, `Program`, `Team Member`.
4. Update Projects via: `Project`, `Project Image`.
5. Update Media via: `Image Gallery`, `Video Gallery`, `Press Release`, `Media Coverage`, `Media Contact`.

## Clean Implementation Notes
- The update keeps existing architecture intact and extends it surgically.
- Unrelated modules were not modified.
- Template/context mismatches were resolved for smooth rendering.
- Code changes avoid unnecessary complexity and preserve maintainability.
