"""
Test the models and functionality related to the models.
"""


from django.test import TestCase
from ..models import User


class TestModel(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating user with an email address is successful"""

        email = "test@example.com"
        password = "testpass123"
        user = User.objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
