import mandrill
import time
from celery import shared_task
from django.conf import settings
from django.template.loader import get_template
from .models import EmailToUser as eu


@shared_task
def send_email(id):
    time.sleep(2)
    EmailToUser = eu.objects.get(id=id)
    template_mail = get_template("mail/{0}.html".format(EmailToUser.email.slug))
    html_email = template_mail.render({
        'EmailToUser': EmailToUser,
    })

    mandrill_client = mandrill.Mandrill(settings.MANDRILL_KEY)
    message = {
        'from_email': EmailToUser.email.sender.email,
        'from_name': EmailToUser.email.sender.name,
        'subject': EmailToUser.email.subject,
        'google_analytics_campaign': EmailToUser.email.slug,
        'google_analytics_domains': ['unmalnick.com'],
        'headers': {'Reply-To': EmailToUser.email.sender.email},
        'tags': [EmailToUser.email.slug],
        'html': html_email,
        'to': [
            {
                'email': EmailToUser.user.email,
                'name': EmailToUser.user.first_name,
                'type': 'to'
            }
        ],
    }
    result = mandrill_client.messages.send(message=message, send_async=False)

    EmailToUser.status = result[0].get('status')
    EmailToUser.reject_reason = result[0].get('reject_reason')
    EmailToUser.message_id = result[0].get('_id')

    EmailToUser.save()

    return None