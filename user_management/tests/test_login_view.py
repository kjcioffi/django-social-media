from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class LoginViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "johndoe", "password": "crdRBDwEGk9Cr03FcPJC"}

        User.objects.create_user(**self.credentials)

    def test_form_in_context(self):
        request = self.client.get(reverse("user_management:login"))
        self.assertTrue(request.context["form"])
        self.assertIsNotNone(request.context["form"])

    def test_user_login(self):
        redirect = self.client.post(
            reverse("user_management:login"), self.credentials, follow=True
        )

        self.assertEqual(redirect.status_code, 200)
        self.assertRedirects(redirect, reverse("content_sharing:index"))
        self.assertTrue(redirect.context["user"].is_authenticated)
