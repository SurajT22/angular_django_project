# views.py or context_processors.py
from django.conf import settings

def site_settings(request):
    return {
        'site_logo': settings.SITE_LOGO_PATH,
        # Add other site-wide settings as needed
    }

from django.http import JsonResponse

def get_logo_path(request):
    logo_path = '/api/logo-path/logo.png'  # Adjust this based on your project structure
    return JsonResponse({'logo_path': logo_path})
