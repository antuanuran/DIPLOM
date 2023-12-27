from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task(autoretry_for=(Exception,), max_retries=3, retry_backoff=5)
def send_email(body, subject, recipient_list):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        recipient_list,
        fail_silently=False,
    )
