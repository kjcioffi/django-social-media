import django.utils.timezone as timezone

from django.contrib.auth.models import User

from django.db import models


class Profile(models.Model):
    """
    Represents a user's social media profile.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=600, blank=True)
    pic = models.ImageField(upload_to='', default='default.jpg')

    def __str__(self) -> str:
        return self.user
    

class Post(models.Model):
    """
    Represents a social media post.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=30000)

    # only records date of creation
    created = models.DateField(auto_now_add=timezone.now().date)

    def __str__(self) -> str:
        return f'Post {self.id} created by {self.profile}'


class PostLike(models.Model):
    """
    Represents a like to a social media post.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.profile} liked post {self.post.id}'