from django.conf import settings

def marketing_ids(request):
    context = {
        'G_ANALYTICS': settings.GOOGLE_ANALYTICS_ID
    }
    return context