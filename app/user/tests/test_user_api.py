"""
Tests the user API

# Endpoints
- HTTP POST `/api/user/create/

# Types of endpoint based on authorization
- public
- private

"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


CREATE_USER_URL = reverse("create")


class PublicUserApiTests(TestCase):
    """Tests the public API endpoints from user API"""

    @staticmethod
    def create_user(**params):
        """returns user from whichever default user model"""

        return get_user_model().objects.create_user(**params)

    def setUp(self) -> None:
        """
        Instantiate client
        """

        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating user is successful (/api/user/create/)"""

        payload = {
            "email": "test@example.com",
            "password": "password@321",
            "name": "Test Name"
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, 201)

    # scenario 2 - short password (len(password) < 5 )
    def test_create_user_with_short_password(self):
        """Test error returned if password is less than 5 characters"""

        payload = {
            "email": "test@example.com",
            "password": "",
            "name": "Test Name"
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, 400)

    # scenario 3 - user email already exists in database
    def test_user_with_email_exists_error(self):
        """Test error returned if user email already exists"""

        payload = {
            "email": "test@example.com",
            "password": "password@321",
            "name": "Test Name"
        }

        # step 1: create user using ORM
        self.create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, 400)



