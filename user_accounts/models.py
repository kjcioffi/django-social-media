from datetime import date
from django.forms import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(blank=False, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=False, max_length=150, verbose_name='last name')
    email = models.EmailField(blank=False, max_length=254, verbose_name='email address')
    birthday = models.DateField(blank=False, auto_now=False, auto_now_add=False)

    def clean_fields(self, exclude=None) -> None:
        if self.birthday is None:
            raise ValidationError({'birthday': 'Birthday cannot be blank.'})

        today = timezone.now().date()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        
        if age < 18:
            raise ValidationError({"birthday": "Must be at least 18 years of age."})
        
        super().clean_fields(exclude=exclude)
