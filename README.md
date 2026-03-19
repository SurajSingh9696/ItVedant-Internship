# NGO CMS

A Django-based NGO Content Management System with role-based access, donation management, volunteer management, blogs, projects, and media pages.

## Features

- Role-based user system: admin, editor, viewer
- Login, registration, email verification, session management, password reset
- NGO pages: home, about, work, projects, media, blog, contact
- Donation flow with Razorpay integration and payment verification
- Volunteer form and newsletter subscription
- Admin dashboard with recent activity
- RESTful API endpoints for content management, form submissions, and donation data

## Tech Stack

- Backend: Django
- Database: MySQL or SQLite locally, PostgreSQL via DATABASE_URL on deployment
- Frontend: Django Templates + Bootstrap
- Payment: Razorpay

## Project Structure

- accounts: authentication and user management
- core: CMS pages, projects, blogs, events, media
- donations: donation forms and payment flow
- volunteers: volunteer and newsletter modules

## REST API

Base path: /api/

- /api/users/
- /api/programs/
- /api/projects/
- /api/blog-posts/
- /api/media-items/
- /api/statistics/
- /api/contacts/
- /api/events/
- /api/donations/
- /api/volunteers/
- /api/newsletter/

Permission behavior:

- Public create access for contact, donation, volunteer, newsletter form APIs
- Admin and editor access for content management writes
- Admin-only access for user management API

## Local Setup

1. Create virtual environment

```powershell
python -m venv .venv
```

2. Install dependencies

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

3. Run migrations

```powershell
.venv\Scripts\python.exe manage.py migrate
```

4. Create admin user

```powershell
.venv\Scripts\python.exe manage.py createsuperuser
```

5. Start server

```powershell
.venv\Scripts\python.exe manage.py runserver
```

App runs at http://127.0.0.1:8000/

## Environment Variables

Create a `.env` file with values:

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DB_ENGINE
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- DATABASE_URL
- RAZORPAY_KEY_ID
- RAZORPAY_KEY_SECRET
- EMAIL_HOST
- EMAIL_PORT
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- DEFAULT_FROM_EMAIL

## Render Deployment

Build command:

```bash
./build.sh
```

Start command:

```bash
gunicorn ngo_cms.wsgi:application
```

Set environment variables in Render dashboard and attach a PostgreSQL database.

## Vercel Note

This Django project is best deployed on Render. Vercel is possible but not ideal for this full Django architecture.
# ItVedant-Internship
