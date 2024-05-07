from django.test import TestCase

from django.contrib.auth.models import User

from content_sharing.models import Post, Profile


class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='johndoe', password='j@hND03')
        self.profile = Profile.objects.create(user=self.user)
        self.post = Post.objects.create(profile=self.profile)
    
    def test_profile_removal_delete_cascades_posts(self):
        self.profile.delete()
        
        self.assertNotIn(self.post, Post.objects.all())

    def test_post_removal_does_not_delete_profile(self):
        self.post.delete()

        self.assertIn(self.profile, Profile.objects.all())

    def test_post_content_not_empty(self):
        pass

    def test_post_has_max_30_chars(self):
        pass

    def test_time_stamp_not_empty(self):
        pass
