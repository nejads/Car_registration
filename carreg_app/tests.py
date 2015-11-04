from django.test import TestCase
from django.core.urlresolvers import reverse
# http://www.django-rest-framework.org/api-guide/status-codes/#status-codes
from rest_framework import status

from .models import *
from .utils import to_json


class IndexViewTests(TestCase):
    def test_index_view_is_working(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'station')


class UsersViewTests(TestCase):
    def setUp(self):
        self.data = {
                'name': 'test_first_name',
                'email': 'test_email@email.com',
                'password': 'test_password',
                'plate': 'test_plate',
                'bank': 'test_bank',
                'tel': '0046705555433',
        }

    def test_user_registration_with_valid_inputs(self):
        response = self.client.post(reverse('api:user_register'),
                                    data=to_json(self.data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], 'test_email@email.com')
