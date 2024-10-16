from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from content_sharing.models import Profile

@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    """
    Creates profile for user upon joining the platform.
    """
    Profile.objects.create(user=user)