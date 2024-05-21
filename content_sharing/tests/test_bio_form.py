from django.test import Client, TestCase

from content_sharing.forms import BioForm
from content_sharing.models import Profile
from content_sharing.tests.utils import TestUtil


class BioFormTest(TestCase):

    def setUp(self):
        self.utils = TestUtil()
        self.bio_max_length = Profile._meta.get_field('bio').max_length

    def test_bio_null_converts_to_empty(self):
        form = BioForm({'bio': None})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean()['bio'], '')

    def test_bio_submitted_empty(self):
        form = BioForm({'bio': ''})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean()['bio'], '')

    def test_bio_accepts_within_600_chars(self):
        bio_contents = self.utils.random_string_generator(self.bio_max_length)
        form = BioForm({'bio': bio_contents})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.clean()['bio'], bio_contents)
    
    def test_bio_rejects_greater_than_600_chars(self):
        bio_contents = self.utils.random_string_generator(self.bio_max_length + 1)
        form = BioForm({'bio': bio_contents})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['bio'], [f'Ensure this value has at most 600 characters (it has {self.bio_max_length + 1}).'])
    