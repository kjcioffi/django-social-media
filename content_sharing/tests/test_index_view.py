import datetime
from django.utils import timezone
from django.test import Client, TestCase
from django.urls import reverse

from django.db.models import QuerySet

from content_sharing.forms import PostForm
from content_sharing.models import Post

from .utils import TestUtil

class IndexViewTest(TestCase):

    def setUp(self):
        self.utils = TestUtil()
        self.profile = self.utils.create_profile(user=self.utils.create_user())

        self.client = Client()
        self.client.login(username=self.profile.user.username, password='j@hND03')
        self.response = self.client.get(reverse('content_sharing:index'))

    def test_correct_form_in_context(self):
        self.assertEqual(self.response.status_code, 200)
        form = self.response.context['post_form']
        self.assertTrue(form)
        self.assertIsInstance(form, PostForm)

    def test_posts_from_past_day_in_context(self):
        self.utils.create_posts(5, self.profile)

        old_post = Post.objects.first()
        old_post.created = timezone.now().date() - datetime.timedelta(days=2)
        old_post.save()

        self.response = self.client.get(reverse('content_sharing:index'))
        
        posts_in_view: QuerySet = self.response.context['posts']
        self.assertNotEqual(posts_in_view.count(), 0)
        self.assertNotIn(old_post, posts_in_view)
    
    def test_user_must_be_logged_in(self):
        self.client.logout()
        self.response = self.client.get(reverse('content_sharing:index'))
        self.assertRedirects(self.response, '/login/?next=/')
