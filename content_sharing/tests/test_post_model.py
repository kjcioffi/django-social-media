import string
import random

from django.forms import ValidationError
from django.test import TestCase

from django.contrib.auth.models import User

from content_sharing.models import Post, Profile


class PostModelTest(TestCase):

    def setUp(self):


        self.user = User.objects.create(username='johndoe', password='j@hND03')
        self.profile = Profile.objects.create(user=self.user)

        self.post = Post.objects.create(profile=self.profile, 
                                        content=''.join(random.choice(string.ascii_letters) for _ in range(50)))
    
    def test_profile_removal_delete_cascades_posts(self):
        self.profile.delete()
        
        self.assertNotIn(self.post, Post.objects.all())

    def test_post_removal_does_not_delete_profile(self):
        self.post.delete()

        self.assertIn(self.profile, Profile.objects.all())

    def test_post_content_not_empty(self):
        post = Post(profile=self.profile, content=None)

        with self.assertRaises(ValidationError) as e:
            post.clean_fields()

        self.assertIn('content', e.exception.error_dict)

    def test_post_has_max_30_chars(self):
        pass

    def test_time_stamp_not_empty(self):
        pass
