from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class BasicTest(TestCase):
    def test_basic_math(self):
        self.assertEqual(1 + 1, 2)
    
    def test_database_connection(self):
        user_count = User.objects.count()
        self.assertGreaterEqual(user_count, 0)

class SimpleAPITest(APITestCase):
    def test_get_polls_list(self):
        response = self.client.get('/api/polls/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AuthenticationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_get_auth_token(self):
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post('/api/auth/token/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
