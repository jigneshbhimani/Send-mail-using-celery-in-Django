from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from send_emails_celery.settings import EMAIL_HOST_USER

@shared_task(bind=True)
def send_mail_func(self):
    mail_subject = "Celery Mail",
    message = "Test mail sent by Django Celery",
    to_mail = 'jignesh.bhimani@creolestudios.com',

    send_mail(
        subject = mail_subject,
        message= message,
        from_email= settings.EMAIL_HOST_USER,
        recipient_list= [to_mail,],
        fail_silently= True,
    )

    return "Mail sent successfully using celery..."