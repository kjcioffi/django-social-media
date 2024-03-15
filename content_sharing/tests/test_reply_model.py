import datetime
from django.test import TestCase

from content_sharing.models import Post, Reply, UserProfile
from user_accounts.models import User

class TestReplyModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='johndoe', first_name='John', last_name='Doe',
                        email='johndoe@example.com', birthday=datetime.date(1900, 1, 1))
        
        self.user_profile = UserProfile.objects.filter(user=self.user).get()

        self.post = Post.objects.create(user_profile=self.user_profile, content="Test post.")

        self.reply = Reply.objects.create(user_profile=self.user_profile, post=self.post)

    def test_user_profiles_delete_cascade_replies(self):
        self.user_profile.delete()
        self.assertNotIn(self.reply, Reply.objects.all())

    def test_replies_dont_delete_cascade_user_profiles(self):
        self.reply.delete()
        self.assertIn(self.user_profile, UserProfile.objects.all())

    def test_posts_delete_cascade_replies(self):
        self.post.delete()
        self.assertNotIn(self.reply, Reply.objects.all())

    def test_replies_dont_delete_cascade_posts(self):
        self.reply.delete()
        self.assertIn(self.post, Post.objects.all())