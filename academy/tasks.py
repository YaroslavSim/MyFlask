"""Tasks."""
import os

from celery import shared_task

from sendgrid import SendGridAPIClient

from sendgrid.helpers.mail import Mail

from hillel_lesson.settings import SENDGRID_API_KEY


@shared_task
def send_email(instance):
    """Send email function."""
    message = Mail(
        from_email='yaroslavsim@ukr.net',
        to_emails='yaroslavsim@gmail.com',
        subject='New message from {}'.format(instance.name),
        html_content='<strong>Name: {}<br>Email: {}<br>Message: {}</strong>'.format(instance.name, instance.email, instance.message)
        )
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
