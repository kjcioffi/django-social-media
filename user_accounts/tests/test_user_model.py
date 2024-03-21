import datetime
import random
import re
import string
from django.forms import ValidationError
from django.test import TestCase

from user_accounts.models import User


class TestUserModel(TestCase):

    def setUp(self):
        self.ascii = string.ascii_letters
        self.user = User(username='johndoe', first_name='John', last_name='Doe',
                        email='johndoe@example.com', birthday=datetime.date(1900, 1, 1),
                        password='temporary123')

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
            self.assertNotIn('birthday', e.error_dict)
            
    
    def test_birthday_blank(self):
        with self.assertRaises(ValidationError) as e:
            self.user.birthday = None
            self.user.full_clean()

        self.assertIn('birthday', e.exception.message_dict)
        for exception in e.exception.message_dict:
            if exception == 'birthday':
                self.assertEqual(e.exception.message_dict['birthday'], ['This field cannot be null.'])

    def test_valid_birthdate_format(self):
        valid_date_pattern = re.compile('^\d{4}-\d{2}-\d{2}$')

        for date in ['1900-01-01', '1980-01-01', '2000-01-01']:
                    self.assertTrue(valid_date_pattern.match(date), f'{date} should be valid.')

                    self.user.birthday = date
                    try:
                        self.user.full_clean()
                    except ValidationError as e:
                        self.fail(f'Valid date {date} should not have raised a ValidationError: {e}')

    def test_invalid_birthdate_format(self):
        expected_error_message = "value has an invalid date format. It must be in YYYY-MM-DD format."
        for date in ['1900-01', '01-01', '1900-01-321', 'abcd-12-34', '1', 'Invalid date']:
            with self.assertRaises(ValidationError) as e:
                self.user.birthday = date
                self.user.full_clean()
            
            actual_message = str(e.exception)
            self.assertIn(expected_error_message, actual_message, f"Expected message not found in error for {date}")

    def test_user_at_least_18_years_old(self):
        with self.assertRaises(ValidationError) as e:
            self.user.birthday = datetime.date(2007, 3, 17)
            self.user.full_clean()

        self.assertIn('birthday', e.exception.message_dict)
        for exception in e.exception.message_dict:
            if exception == 'birthday':
                self.assertEqual(e.exception.message_dict['birthday'], ['Must be 18 years or older to sign up.'])