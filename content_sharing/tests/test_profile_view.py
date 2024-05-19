from django.test import Client, TestCase
from django.urls import reverse

from content_sharing.tests.utils import TestUtil


class ProfileViewTest(TestCase):

    def setUp(self):
        self.util = TestUtil()
        self.user = self.util.create_user()
        self.profile = self.util.create_profile(user=self.user)
        self.response = self.util.get_request('content_sharing:profile', self.profile.user.username)

    def test_login_required(self):
        self.util.logout()
        response = self.util.get_request('content_sharing:profile', self.profile.user.username)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(response, f'/login/?next=/{self.profile.user.username}')

    def test_profile_populates_by_username(self):
        context_profile = self.response.context['profile']
        self.assertEqual(context_profile.user.username, self.profile.user.username)
