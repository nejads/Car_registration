import os
from base64 import b64encode
import smtplib

from django.core.mail import send_mail


from rest_framework.renderers import JSONRenderer


def validate_phone():
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Not allowed telephone number")


def salt_gen():
    random_bytes = os.urandom(32)
    random_string = b64encode(random_bytes).decode('utf-8')
    return random_string


def to_json(dictionary):
    json = JSONRenderer().render(dictionary)
    return json


def send_mail(email):
    try:
        send_mail('Welcome to WAAP!',
                  message_plain,
                  'no-reply@waap.com',
                  [email],
                  html_message=message_html)
    except (smtplib.SMTPException) as e:
        return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
