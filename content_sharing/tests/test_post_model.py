import datetime
import random
import string
from django.forms import ValidationError
from django.test import TestCase

from content_sharing.models import Post, UserProfile
from user_accounts.models import User

class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='johndoe', first_name='John', last_name='Doe',
                        email='johndoe@example.com', birthday=datetime.date(1900, 1, 1))
        
        self.user_profile = UserProfile.objects.filter(user=self.user).get()

        self.post = Post.objects.create(user_profile=self.user_profile, content='')

    def test_user_profile_on_post_not_empty(self):
        self.post.user_profile = None
        with self.assertRaises(ValidationError) as e:
            self.post.clean_fields()
        self.assertIn('user_profile', e.exception.message_dict)

    def test_post_content_not_empty(self):
        with self.assertRaisesMessage(ValidationError, "{'content': ['This field cannot be blank.']}"):
            self.post.clean_fields()

    def test_post_content_max_30k_chars(self):
        letters = string.ascii_letters
        with self.assertRaisesMessage(ValidationError, "{'content': ['Ensure this value has at most 30000 characters (it has 30001).']}"):
            self.post.content = ''.join(random.choice(letters) for _ in range(30001))
            self.post.clean_fields()

    def test_user_profile_delete_cascades_posts(self):
        self.user_profile.delete()
        self.assertNotIn(self.post, Post.objects.all())

    def test_post_does_not_delete_cascade_user_profiles(self):
        self.post.delete()
        self.assertIn(self.user_profile, UserProfile.objects.all())
        