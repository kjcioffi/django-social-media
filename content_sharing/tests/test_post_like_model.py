import random
import string

from content_sharing.models import Profile, Post, PostLike

from django.contrib.auth.models import User

from django.test import TestCase


class PostLikeModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='johndoe', password='j@hND03')
        self.profile = Profile.objects.create(user=self.user)

        self.post = Post.objects.create(profile=self.profile, 
                                        content=''.join(random.choice(string.ascii_letters) for _ in range(50)))
        
        self.post_like = PostLike.objects.create(profile=self.profile, post=self.post)

    def test_profile_delete_cascades_likes(self):
        self.profile.delete()

        self.assertNotIn(self.post_like, PostLike.objects.all())

    def test_likes_deletion_does_not_delete_profile(self):
        self.post_like.delete()

        self.assertIn(self.profile, Profile.objects.all())

    def test_post_delete_cascades_likes(self):
        self.post.delete()

        self.assertNotIn(self.post_like, PostLike.objects.all())

    def test_like_deletion_does_not_delete_post(self):
        self.post_like.delete()

        self.assertIn(self.post, Post.objects.all())
    