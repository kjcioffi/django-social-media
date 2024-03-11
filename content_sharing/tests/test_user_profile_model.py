import datetime
import random
import string
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import ValidationError
from django.test import TestCase

from content_sharing.models import UserProfile, user_directory_path
from user_accounts.models import User

class TestUserProfileModel(TestCase):

    def setUp(self):
        self.user = User(username='johndoe', first_name='John', last_name='Doe',
                        email='johndoe@example.com', birthday=datetime.date(1900, 1, 1))
        
        self.user.save()
        
        self.user_profile = UserProfile(user=self.user, bio="")

    def test_empty_bio(self):
        self.user_profile.bio = None
        self.assertEqual(self.user_profile.bio, None)

    def test_bio_not_empty(self):
       self.user_profile.bio = """
                                Just a guy exploring the world one day at a time.
                                Love photography, hiking, and all things tech. 
                                Living life in pursuit of the next adventure. 🌆🌲💻
                                """
       
       self.assertNotEquals(self.user_profile.bio, None)

    def test_bio_not_greater_than_600_chars(self):
        letters = string.ascii_letters

        with self.assertRaises(ValidationError) as e:
            self.user_profile.bio = ''.join(random.choice(letters) for _ in range(601))
            self.user_profile.full_clean()
            
        self.assertIn('bio', e.exception.message_dict)

    def test_default_image(self):
        self.user_profile.save()
        self.assertEqual(self.user_profile.photo, 'default.jpg')

    def test_no_default_image(self):
        self.user_profile.photo = SimpleUploadedFile(name='test_image.jpg', content=b'' * 1024, content_type='image/jpeg')
        self.user_profile.save()
        self.assertTrue(UserProfile.objects.get(user=self.user).photo, 'test_image.jpg')

    def test_proper_save_location(self):
        self.user_profile.photo = SimpleUploadedFile(name='test_image.jpg', content=b'' * 1024, content_type='image/jpeg')
        self.user_profile.save()

        expected_path = user_directory_path(self.user_profile, 'test_image.jpg')
        self.assertTrue(self.user_profile.photo, expected_path)
        