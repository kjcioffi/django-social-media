import datetime
from django.contrib.messages.test import MessagesTestMixin
from django.contrib import messages
from django.test import Client, TestCase
from django.urls import reverse

class TestUserLoginView(TestCase):

    def setUp(self):
        self.client = Client()
        self.form_data = {'username': 'johndoe',
                          'first_name': 'john',
                          'last_name': 'doe',
                          'email': 'johndoe@example.com',
                          'birthday': datetime.date(1900, 1, 1),
                          'password1': 'temporary123',
                          'password2': 'temporary123'}
        
        self.request = self.client.post(reverse('user_accounts:sign-up'), self.form_data)


    def test_messages_in_context(self):
        login_page = self.client.get(self.request.url)
        self.assertRedirects(self.request, '/login/')
        messages = list(login_page.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Your account was successfully created, feel free to login!')