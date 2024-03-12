import datetime
import random
import string
from django.forms import ValidationError
from django.test import TestCase

from content_sharing.models import Post, UserProfile
from user_accounts.models import User

class TestPostModel(TestCase):

    def setUp(self):
        self.user = User(username='johndoe', first_name='John', last_name='Doe',
                        email='johndoe@example.com', birthday=datetime.date(1900, 1, 1))
        
        self.user.save()
        
        self.user_profile = UserProfile(user=self.user, bio="")
        self.user_profile.save()

        self.post = Post(user_profile=self.user_profile, content='')

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
