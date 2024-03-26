from django.test import Client, TestCase
from django.urls import reverse

from content_sharing.models import UserProfile
from user_accounts.models import User

class TestHomePageView(TestCase):

    def login_user(self, username='johndoe', password='temporary123'):
        self.client.login(username=username, password=password)
        self.response = self.client.get(reverse('content_sharing:home_page'))

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='johndoe', first_name='John',
                                        last_name='Doe', email='johndoe@example.com',
                                        birthday='1900-01-01',
                                        password='temporary123')
        
        self.login_user()

    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        self.response = self.client.get(reverse('content_sharing:home_page'))
        self.assertEqual(self.response.status_code, 302)
        self.assertTrue(self.response.url.startswith('/login'))

    def test_access_with_authenticated_user(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.request['PATH_INFO'], '/')

    def test_form_in_context(self):
        self.assertIn('form', self.response.context)

    def test_form_bound_when_posted(self):
        data={'content': 'Today is a beautiful day to go outside and enjoy the fresh air. What are your plans for today?'}
        response = self.client.post(reverse('content_sharing:home_page'), data)
        print(response)
        
    def test_form_not_bound_on_page_load(self):
        form = self.response.context['form']
        self.assertIsNotNone(form)
        self.assertFalse(form.is_bound, 'Form should be empty when page loads.')

    def test_create_new_post(self):
        pass

    def test_get_posts_ordered_by_latest_timestamp(self):
        pass

    def test_comment_button_drops_down_comment_form(self):
        pass

    def test_comment_persists_when_posted(self):
        pass
    