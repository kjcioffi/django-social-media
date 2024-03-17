import datetime
import re
from django.test import Client, TestCase
from django.urls import reverse

from user_accounts.forms import UserSignUpForm
from user_accounts.models import User


class TestUserSignUpView(TestCase):

    def setUp(self):
        self.client = Client()
        self.form_data = {'username': 'johndoe',
                          'first_name': 'john',
                          'last_name': 'doe',
                          'email': 'johndoe@example.com',
                          'birthday': datetime.date(1900, 1, 1),
                          'password1': 'temporary123',
                          'password2': 'temporary123'}

        self.response = self.client.get(reverse('user_accounts:sign-up'))
        
    def test_form_in_view_context(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertIn('form', self.response.context, 'The form should be available via context.')

    def test_form_submit_success(self):
        request = self.client.post(reverse('user_accounts:sign-up'), self.form_data)
        self.assertEqual(request.status_code, 302)
        user = User.objects.filter(username=self.form_data['username'])
        self.assertTrue(user.exists(), 'The user should save after submission.')

    def test_form_submit_fails_with_blank_fields(self):
        bad_form_data = {'username': '',
                          'first_name': '',
                          'last_name': '',
                          'email': '',
                          'birthday': '',
                          'password1': '',
                          'password2': ''}
        
        request = self.client.post(reverse('user_accounts:sign-up'), bad_form_data)
        form = request.context['form']

        self.assertFormError(form, 'username', 'This field is required.')
        self.assertFormError(form, 'first_name', 'This field is required.')
        self.assertFormError(form, 'last_name', 'This field is required.')
        self.assertFormError(form, 'email', 'This field is required.')
        self.assertFormError(form, 'birthday', ['This field is required.', 'Birthday cannot be blank.'])
        self.assertFormError(form, 'password1', 'This field is required.')
        self.assertFormError(form, 'password2', 'This field is required.')
