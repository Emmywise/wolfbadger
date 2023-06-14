from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from accounts.models import UserProfile


class UserProfileTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user_profile = UserProfile.objects.create(user=self.user)  # Create the user profile
        self.client.login(username=self.username, password=self.password)


    def test_user_profile_creation(self):
        # Ensure user profile is created for the logged-in user
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['profile'].userprofile, UserProfile)

    def test_user_profile_retrieval(self):
        # Ensure user profile information is displayed correctly
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.username)

    def test_user_profile_update(self):
        # Ensure user profile information is updated successfully
        new_name = 'John Doe'
        response = self.client.post(reverse('profile_update'), {'name': new_name})
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.userprofile.name, new_name)

    def test_user_profile_deletion(self):
        # Ensure user profile is deleted
        response = self.client.post(reverse('delete_profile'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(UserProfile.objects.filter(user=self.user).exists())
