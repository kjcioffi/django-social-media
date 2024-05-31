from django.test import Client, TestCase

from content_sharing.tests.utils import TestUtil


class LogoutViewTest(TestCase):

    def setUp(self):
        self.util = TestUtil()
        self.profile = self.util.create_profile(self.util.create_user())
        self.response = self.util.post_request("user_management:logout")

    def test_user_logs_out_after_post(self):
        self.assertFalse(self.response.wsgi_request.user.is_authenticated)

    def test_user_redirected_to_login_after_logout(self):
        self.assertRedirects(self.response, "/login/")
