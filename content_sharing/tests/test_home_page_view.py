from django.test import Client, TestCase
from django.urls import reverse

from user_accounts.models import User

class TestHomePageView(TestCase):

    def setUp(self):
        self.client = Client()
        self.request = self.client.get(reverse('content_sharing:home_page'))
        self.user = User.objects.create_user(username='johndoe', first_name='John',
                                        last_name='Doe', email='johndoe@example.com',
                                        birthday='1900-01-01',
                                        password='temporary123')

    def test_redirect_if_not_logged_in(self):
        self.assertEqual(self.request.status_code, 302)
        self.assertTrue(self.request.url.startswith('/login'))

    def test_access_with_authenticated_user(self):
        self.client.login(username=self.user.username, password='temporary123')
        self.request = self.client.get(reverse('content_sharing:home_page'))
        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(self.request.request['PATH_INFO'], '/')

    def test_create_new_post(self):
        pass

    def test_get_posts_ordered_by_latest_timestamp(self):
        pass

    def test_comment_button_drops_down_comment_form(self):
        pass

    def test_comment_persists_when_posted(self):
        pass
    