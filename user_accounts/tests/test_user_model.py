import datetime
import random
import string
from django.forms import ValidationError
from django.test import TestCase

from user_accounts.models import User


class TestUserModel(TestCase):

    def setUp(self):
        self.ascii = string.ascii_letters
        self.user = User(username='johndoe', first_name='John', last_name='Doe',
                        email='johndoe@example.com', birthday=datetime.date(1900, 1, 1))

    def test_first_name_not_blank(self):
        try:
            self.user.full_clean()
        except ValidationError as e:
            if 'first_name' in e.message_dict:
                self.fail(f'A ValidationError was raised for a non-blank first name: {e.message_dict}')
    
    def test_first_name_blank(self):
        with self.assertRaises(ValidationError) as e:
            self.user.first_name = None
            self.user.full_clean()
        self.assertIn('first_name', e.exception.message_dict)
    
    def test_first_name_within_150_chars(self):
        with self.assertRaises(ValidationError) as e:
            self.user.first_name = ''.join(random.choice(self.ascii) for _ in range(151))
            self.user.full_clean()
        self.assertIn('first_name', e.exception.message_dict)

    def test_last_name_not_blank(self):
        try:
            self.user.full_clean()
        except ValidationError as e:
            if 'last_name' in e.message_dict:
                self.fail(f'A ValidationError was raised for a non-blank last name: {e.message_dict}')

    def test_last_name_blank(self):
        with self.assertRaises(ValidationError) as e:
            self.user.last_name = None
            self.user.full_clean()
        self.assertIn('last_name', e.exception.message_dict)

    def test_last_name_within_150_chars(self):
        with self.assertRaises(ValidationError) as e:
            self.user.last_name = ''.join(random.choice(self.ascii) for _ in range(151))
            self.user.full_clean()
        self.assertIn('last_name', e.exception.message_dict)

    def test_email_not_blank(self):
        try:
            self.user.full_clean()
        except ValidationError as e:
            if 'email' in e.message_dict:
                self.fail(f'A ValidatioNError was raised for non-blank email: {e.message_dict}')
    
    def test_email_blank(self):
        with self.assertRaises(ValidationError) as e:
            self.user.email = None
            self.user.full_clean()
        self.assertIn('email', e.exception.message_dict)

    def test_email_within_254_chars(self):
        with self.assertRaises(ValidationError) as e:
            self.user.email = ''.join(random.choice(self.ascii) for _ in range(255))
            self.user.full_clean()
        self.assertIn('email', e.exception.message_dict)

    def test_birthday_not_blank(self):
        try:
            self.user.full_clean()
        except ValidationError as e:
            if 'birthday' in e.message_dict:
                self.fail(f'A ValidatioNError was raised for non-blank birthday: {e.message_dict}')
    
    def test_birthday_blank(self):
        with self.assertRaisesMessage(ValidationError, "{'birthday': ['Birthday cannot be blank.']}"):
            self.user.birthday = None
            self.user.clean_fields()

    def test_user_older_than_18_years_old(self):
        with self.assertRaisesMessage(ValidationError, "{'birthday': ['Must be at least 18 years of age.']}"):
            self.user.birthday = datetime.date(2007, 3, 11)
            self.user.full_clean()
