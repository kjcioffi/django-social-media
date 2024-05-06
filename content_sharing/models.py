from django.db import models


class Profile(models.Model):
    bio = models.CharField(max_length=600, blank=True)
