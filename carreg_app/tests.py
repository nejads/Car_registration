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

    def test_user_registration_with_invalid_inputs(self):
        bad_data = {
                'email': 'test_email@email.com',
                'password': 'test_password',
                'plate': 'test_plate',
                'bank': 'test_bank',
                'tel': '0046705555433',
        }
        response = self.client.post(reverse('api:user_register'),
                                    data=to_json(bad_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_registration_with_duplicate_valid_inputs(self):
        response2 = self.client.post(reverse('api:user_register'),
                                     data=to_json(self.data),
                                     content_type='application/json')
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        response3 = self.client.post(reverse('api:user_register'),
                                     data=to_json(self.data),
                                     content_type='application/json')
        self.assertEqual(response3.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login_with_valid_inputs(self):
        response = self.client.post(reverse('api:user_register'),
                                    data=to_json(self.data),
                                    content_type='application/json')
        response_login = self.client.post(reverse('api:user_login'),
                                          data=to_json(self.data),
                                          content_type='application/json')
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)

    def test_user_login_with_invalid_inputs(self):
        bad_data = {
                'email': 'test_email@email.com',
                'password': 'wrong_password',
        }
        response = self.client.post(reverse('api:user_register'),
                                    data=to_json(self.data),
                                    content_type='application/json')
        response_login = self.client.post(reverse('api:user_login'),
                                          data=to_json(bad_data),
                                          content_type='application/json')
        self.assertEqual(response_login.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_login_with_not_existing_inputs(self):
        response = self.client.post(reverse('api:user_register'),
                                    data=to_json(self.data),
                                    content_type='application/json')
        not_data = {
                'email': 'not_existing@email.com',
                'password': 'test_password',
        }
        response_login = self.client.post(reverse('api:user_login'),
                                          data=to_json(not_data),
                                          content_type='application/json')
        self.assertEqual(response_login.status_code, status.HTTP_404_NOT_FOUND)


