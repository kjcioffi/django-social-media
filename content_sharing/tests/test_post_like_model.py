import datetime
from django.test import TestCase
from content_sharing.models import Post, PostLike, UserProfile

from user_accounts.models import User

class TestPostLikeModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='johndoe', first_name='John', last_name='Doe',
                        email='johndoe@example.com', birthday=datetime.date(1900, 1, 1))
        
        self.user_profile = UserProfile.objects.filter(user=self.user).get()

        self.post = Post.objects.create(user_profile=self.user_profile, content="Test post.")

        self.post_like = PostLike.objects.create(user_profile=self.user_profile, post=self.post)

    def test_user_profile_delete_cascades_to_post_likes(self):
        self.user_profile.delete()
        self.assertNotIn(self.post_like, PostLike.objects.all())

    def test_post_like_does_not_delete_cascade_user_profiles(self):
        self.post_like.delete()
        self.assertIn(self.user_profile, UserProfile.objects.all())

    def test_post_delete_cascades_to_post_likes(self):
        self.post.delete()
        self.assertNotIn(self.post_like, PostLike.objects.all())

    def test_post_like_does_not_delete_cascade_posts(self):
        self.post_like.delete()
        self.assertIn(self.post, Post.objects.all())
