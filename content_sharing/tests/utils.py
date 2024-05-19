from django.test import Client
from django.urls import reverse
from content_sharing.models import Post, Profile

from django.contrib.auth.models import User


class TestUtil():

    def __init__(self):
        self.client = Client()

    def create_posts(self, number_of_posts: int, profile: Profile):
        """
        Create social media posts for tests.

        Pass profile model object to prevent DB prime key collisions.
        """
        for _ in range(number_of_posts):
            Post.objects.create(profile=profile)

    def get_request(self, path: str, *args, **kwargs):
        return self.client.get(reverse(path, args=args, kwargs=kwargs))

    def create_profile(self, user: User):
        return Profile.objects.create(user=user)

    def create_user(self):
        user = User.objects.create_user(username='johndoe', password='j@hND03')
        self.client.login(username=user.username, password='j@hND03')
        return user
    
    def logout(self):
        self.client.logout()
    