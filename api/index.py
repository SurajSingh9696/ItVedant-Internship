import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ngo_cms.settings')

import django
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

django.setup()

if os.environ.get('VERCEL_AUTO_MIGRATE', '1') == '1':
    call_command('migrate', interactive=False, run_syncdb=True, verbosity=0)

app = get_wsgi_application()
