import os
from base64 import b64encode

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
