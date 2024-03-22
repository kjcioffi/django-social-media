from datetime import date
from django.forms import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, birthday, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, email, birthday, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, birthday=birthday, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, birthday, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username, email, birthday, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, birthday, password, **extra_fields)
    

class User(AbstractUser):
    first_name = models.CharField(blank=False, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=False, max_length=150, verbose_name='last name')
    email = models.EmailField(blank=False, max_length=254, verbose_name='email address')
    birthday = models.DateField(blank=False, auto_now=False, auto_now_add=False)

    objects = CustomUserManager()

    def clean_fields(self, exclude=None) -> None:    
        super().clean_fields(exclude=exclude)

        if self.birthday not in (exclude or []) and self.birthday is not None:
            today: date = timezone.now().date()
            age: int = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

            if age < 18:
                raise ValidationError({'birthday': ['Must be 18 years or older to sign up.']})
            