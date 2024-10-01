from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class AuthTestCase(APITestCase):
    def test_users_register_post(self):
        response = self.client.post(
            "/users/register/",
            {"username": "test", "password": "test"},
        ).json()
        self.assertEqual(response, {"username": "test"})

    def test_users_login_post(self):
        get_user_model().objects.create_user(username="test", password="test")
        response = self.client.post(
            "/users/login/",
            {"username": "test", "password": "test"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
