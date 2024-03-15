import datetime
from django.test import TestCase
from content_sharing.models import Post, Reply, ReplyLike, UserProfile

from user_accounts.models import User

class TestReplyLikeModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='johndoe', first_name='John', last_name='Doe',
                        email='johndoe@example.com', birthday=datetime.date(1900, 1, 1))
        
        self.user_profile = UserProfile.objects.filter(user=self.user).get()

        self.post = Post.objects.create(user_profile=self.user_profile, content="Test post.")

        self.reply = Reply.objects.create(user_profile=self.user_profile, post=self.post, response="Test reply.")

        self.reply_like = ReplyLike.objects.create(user_profile=self.user_profile, reply=self.reply)

    def test_user_profiles_delete_cascade_reply_likes(self):
        self.user_profile.delete()
        self.assertNotIn(self.reply_like, ReplyLike.objects.all())

    def test_reply_likes_dont_delete_cascade_user_profiles(self):
        self.reply_like.delete()
        self.assertIn(self.user_profile, UserProfile.objects.all())
    
    def test_replies_delete_casacade_reply_likes(self):
        self.reply.delete()
        self.assertNotIn(self.reply_like, ReplyLike.objects.all())

    def test_reply_likes_dont_delete_cascade_replies(self):
        self.reply_like.delete()
        self.assertIn(self.reply, Reply.objects.all())

