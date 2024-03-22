from django.test import Client, TestCase

from content_sharing.forms import PostForm
from content_sharing.models import Post, UserProfile
from user_accounts.models import User

class TestPostForm(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('johndoe', 'johndoe@example.com', '1900-01-01')
        self.form_data = {'content': 'Test Post.'}

    def test_post_form_invalid(self):
        self.form_data['content'] = "\t\n"
        self.form = PostForm(self.form_data)
        self.assertFalse(self.form.is_valid(), 'Form should only contain characters.')

    def test_post_form_valid(self):
        self.form = PostForm(self.form_data)
        self.assertTrue(self.form.is_valid(), 'Form should be valid.')

    def test_post_form_saves(self):
        self.form = PostForm(self.form_data)
        self.assertTrue(self.form.is_valid(), 'Form should be valid.')
        post = self.form.save(commit=False)
        post.user_profile = UserProfile.objects.get(user=self.user)
        post.save()
        self.assertIsNotNone(Post.objects.get(id=post.id))