from django.db import models

from user_accounts.models import User

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=600, blank=True)
    photo = models.ImageField(upload_to=user_directory_path,
                              default='default.jpg')
    