"""
Test the models and functionality related to the models.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModel(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating user with an email address is successful"""

        email = "test@example.com"
        password = "testpass123"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is in normalized format for any new user"""

        password = "password@321"
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, password)
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email address raises
        ValueError


        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                "",
                "password@321"
            )

        """

        self.assertRaises(
            ValueError, get_user_model().objects.create_user, "", "password@321"
        )

    def test_create_super_user(self):
        """Test creating a superuser"""

        user = get_user_model().objects.create_superuser(
            "test@example.com", "password@321"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
