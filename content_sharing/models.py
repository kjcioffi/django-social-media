from django.contrib.auth.models import User

from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=600, blank=True)
    pic = models.ImageField(upload_to='', default='default.jpg')
    