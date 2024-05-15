from content_sharing.models import Post, Profile

from django.contrib.auth.models import User


class TestUtil():

    def create_posts(self, number_of_posts: int, profile: Profile):
        """
        Create social media posts for tests.

        Pass profile model object to prevent DB prime key collisions.
        """
        for _ in range(number_of_posts):
            Post.objects.create(profile=profile)

    def create_profile(self, user: User):
        return Profile.objects.create(user=user)

    def create_user(self):
        return User.objects.create_user(username='johndoe', password='j@hND03')
    