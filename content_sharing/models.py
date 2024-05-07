import django.utils.timezone as timezone

from django.contrib.auth.models import User

from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=600, blank=True)
    pic = models.ImageField(upload_to='', default='default.jpg')
    

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=30000)
    created = models.DateField(auto_now_add=timezone.now().date)


class PostLike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
