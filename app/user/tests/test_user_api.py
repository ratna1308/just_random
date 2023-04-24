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
from rest_framework import status


CREATE_USER_URL = reverse("create")
TOKEN_URL = reverse("token")
ME_URL = reverse("me")


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

    def test_create_token_for_user(self):
        """Test generates a token for valid user credentials"""

        payload = {
            "email": "test@example.com",
            "password": "password@321",
        }

        self.create_user(**payload)

        res = self.client.post(TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("token", res.data)

    def test_retrive_user_unauthorized(self):
        """Test authentication is required for the user"""

        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_bad_credentials(self):
        """Test returns error if credentials invalid."""

        self.create_user(email='test@example.com', password='goodpass')
        payload = {'email': 'test@example.com', 'password': 'badpass'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_email_not_found(self):
        """Test error returned if user not found for given email."""

        payload = {'email': 'test@example.com', 'password': 'pass123'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """Test posting a blank password returns an error."""

        payload = {'email': 'test@example.com', 'password': ''}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """Test authentication is required for users."""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


