from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User

from django.urls import reverse

from content_sharing.models import Profile


class RegisterViewTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.response = self.client.post(reverse('user_management:register'),
                                         {'username': 'johndoe', 'password1': 'crdRBDwEGk9Cr03FcPJC',
                                                                 'password2': 'crdRBDwEGk9Cr03FcPJC'})

    def test_form_in_context(self):
        request = self.client.get(reverse('user_management:register'))
        self.assertTrue(request.context['form'])

    def test_successful_user_creation(self):
        self.assertEqual(self.response.status_code, 302)
        
        try:
            user = User.objects.filter(username='johndoe')
            self.assertIsNotNone(user)
        except User.DoesNotExist:
            self.fail('User not created like expected.')

    def test_successful_user_creation(self):
        self.assertEqual(self.response.status_code, 302)
        
        try:
            user = User.objects.get(username='johndoe')
            profile = Profile.objects.get(user=user)
            
            self.assertIsNotNone(profile)
            self.assertEqual(profile.user, user)

        except Profile.DoesNotExist:
            self.fail('Profile not created like expected.')
            
        except User.DoesNotExist:
            self.fail('User not created like expected.')

    def test_redirect_to_login(self):
        redirect = self.client.post(reverse('user_management:register'),
                                    {'username': 'maryjane', 'password1': 'crdRBDwEGk9Cr03FcPJC',
                                                               'password2': 'crdRBDwEGk9Cr03FcPJC'},
                                                               follow=True)
        
        self.assertEqual(redirect.status_code, 200)
        self.assertRedirects(redirect, reverse('user_management:login'))
