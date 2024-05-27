import string
import random

from django.forms import ValidationError
from django.test import TestCase

from django.contrib.auth.models import User
from content_sharing.models import Profile


class UserProfileModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='johndoe', password='j@hND03')
        self.profile = Profile.objects.create(user=self.user)

    def test_user_delete_cascades_user_profiles(self):
        self.user.delete()
        self.assertNotIn(self.profile, Profile.objects.all())

    def test_user_profile_does_not_delete_cascade_users(self):
        self.profile.delete()
        self.assertIn(self.user, User.objects.all())

    def test_bio_empty_on_default(self):
        self.assertEqual(len(self.profile.bio), 0)

    def test_bio_not_empty(self):
       self.profile.bio = """
                                Just exploring the world one day at a time.
                                Love photography, hiking, and all things tech. 
                                Living life in pursuit of the next adventure. 🌆🌲💻
                                """
       
       self.assertNotEquals(self.profile.bio, None)

    def test_bio_max_600_chars(self):
        max_length: int = self.profile._meta.get_field('bio').max_length
        
        with self.assertRaises(ValidationError) as e:
            self.profile.bio = ''.join(random.choice(string.ascii_letters) for _ in range(max_length + 1))
            self.profile.full_clean()
            
        self.assertIn('bio', e.exception.error_dict, f'Bio field must be within {max_length} characters')

    def test_profile_picture_has_default_upon_creation(self):
        self.assertEqual(self.profile.pic.url, '/media/default.png')