from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(blank=False, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=False, max_length=150, verbose_name='last name')
    email = models.EmailField(blank=False, max_length=254, verbose_name='email address')
