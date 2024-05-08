from django.test import TestCase
from django.test import Client
from django.urls import reverse

class RegisterViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_form_in_context(self):
        request = self.client.get(reverse('user_management:register'))
        self.assertTrue(request.context['form'])

    def test_successful_user_creation(self):
        pass

    def test_redirect_to_login(self):
        pass
