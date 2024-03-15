from django.db.models.signals import post_save
from django.dispatch import Signal, receiver
from content_sharing.models import UserProfile
from user_accounts.models import User

@receiver(post_save, sender=User)
def create_user_profile_alongside_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)