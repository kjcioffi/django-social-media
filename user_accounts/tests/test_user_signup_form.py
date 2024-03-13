import datetime
from django.test import TestCase

from user_accounts.forms import UserSignUpForm
from user_accounts.models import User

class TestUserSignUpForm(TestCase):

    def setUp(self):
        self.form_data = {'username': 'johndoe',
                          'first_name': 'john',
                          'last_name': 'doe',
                          'email': 'johndoe@example.com',
                          'birthday': datetime.date(1900, 1, 1),
                          'password1': 'temporary123',
                          'password2': 'temporary123'}
        
    def validate_user_form_invalid(self, property, *values):
        for value in values:
            self.form_data[property] = value
            form = UserSignUpForm(self.form_data)
            self.assertFalse(form.is_valid(), f"Form should be invalid.")
        
    def test_bad_first_name(self):
        self.validate_user_form_invalid('first_name', None, '')

    def test_bad_last_name(self):
        self.validate_user_form_invalid('last_name', None, '')

    def test_bad_email(self):
        self.validate_user_form_invalid('email', None, 'john.doe.example.com')

    def test_bad_birthday(self):
        self.validate_user_form_invalid('birthday', None, '', '10-25-2006')

    def test_form_valid(self):
        form = UserSignUpForm(self.form_data)
        self.assertTrue(form.is_valid(), 'The form should be valid. Errors: {0}'.format(form.errors))

    def test_user_saves_successfully(self):
        form = UserSignUpForm(self.form_data)
        user = form.save()
        self.assertIn(user, User.objects.all())
