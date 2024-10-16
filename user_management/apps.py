from django.core.signals import request_finished
from django.apps import AppConfig


class UserManagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_management"

    def ready(self):
        from . import signals

        request_finished.connect(signals.create_user_profile)
