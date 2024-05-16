import random
import string

from django.utils import timezone
from django.http import HttpResponseNotAllowed
from django.test import Client, TestCase
from .utils import TestUtil
from django.urls import reverse

from django.contrib.auth.models import AnonymousUser

from content_sharing.models import Post


class CreatePostView(TestCase):

    def setUp(self):
        self.max_length = Post._meta.get_field('content').max_length
        self.data = {'content':
                     ''.join(random.choice(string.ascii_letters) for _ in range(self.max_length))}

        self.client = Client()
        self.utils = TestUtil()
        self.user = self.utils.create_user()
        self.profile = self.utils.create_profile(self.user)
        self.client.login(username=self.user.username, password='j@hND03')

    def test_view_rejects_get_request(self):
        response = self.client.get(reverse('content_sharing:create_post'))
        self.assertIsInstance(response, HttpResponseNotAllowed)

    def test_view_rejects_delete_request(self):
        response = self.client.delete(reverse('content_sharing:create_post'))
        self.assertIsInstance(response, HttpResponseNotAllowed)

    def test_view_rejects_put_request(self):
        response = self.client.put(reverse('content_sharing:create_post'))
        self.assertIsInstance(response, HttpResponseNotAllowed)

    def test_view_rejects_patch_request(self):
        response = self.client.patch(reverse('content_sharing:create_post'))
        self.assertIsInstance(response, HttpResponseNotAllowed)

    def test_view_accepts_post_request(self):
        response = self.client.post(reverse('content_sharing:create_post'), self.data)
        self.assertNotIsInstance(response, HttpResponseNotAllowed)

    def test_post_created_successfully(self):
        response = self.client.post(reverse('content_sharing:create_post'), self.data)
        self.assertEqual(response.status_code, 201)
        
        self.assertIsNotNone(response.wsgi_request.user)
        
        json = response.json()
        created = timezone.now().date()

        self.assertEqual({'creator': response.wsgi_request.user.username, 'content': self.data['content'], 'created': created.isoformat()}, json)

    def test_exceeded_max_length(self):
        self.max_length += 1
        self.data = {'content':
                     ''.join(random.choice(string.ascii_letters) for _ in range(self.max_length))}
        

        response = self.client.post(reverse('content_sharing:create_post'), self.data)
        self.assertEqual(response.status_code, 400)
        
        json = response.json()
        self.assertEqual({'failure': 'value too long for type character varying(30000)\n'}, json)

    def test_user_logged_out(self):
        self.client.logout()

        response = self.client.post(reverse('content_sharing:create_post'), self.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.wsgi_request.user.username, AnonymousUser.username)
