import random
import string

from django.contrib.auth.models import User
from django.test import TestCase

from content_sharing.forms import PostForm
from content_sharing.models import Post, Profile


class PostFormTest(TestCase):

    def setUp(self):
        self.data = {}

    def test_post_submitted_empty(self):
        post = PostForm({"content": ""})
        self.assertFalse(post.is_valid(), "Post should be invalid if content is empty.")
        self.assertEqual(post.errors["content"], ["This field is required."])

    def test_post_not_null(self):
        self.data["content"] = None
        post = PostForm(self.data)

        self.assertFalse(
            post.is_valid(), "Post should be invalid if content is null (None)."
        )
        self.assertEqual(post.errors["content"], ["This field is required."])

    def test_post_rejects_30k_plus_chars(self):
        max_content_length = Post._meta.get_field("content").max_length
        self.data["content"] = "".join(
            random.choice(string.ascii_letters) for _ in range(max_content_length + 1)
        )
        post = PostForm(self.data)

        self.assertFalse(post.is_valid())
        self.assertEqual(
            post.errors["content"],
            [
                f"Ensure this value has at most 30000 characters (it has {max_content_length + 1})."
            ],
        )

    def test_post_valid_with_30k_chars(self):
        max_content_length = Post._meta.get_field("content").max_length
        self.data["content"] = "".join(
            random.choice(string.ascii_letters) for _ in range(max_content_length)
        )
        form = PostForm(self.data)

        self.assertTrue(
            form.is_valid(),
            "Post should be valid because it is within the character length.",
        )

        if form.is_valid():
            self.assertEqual(form.cleaned_data["content"], self.data["content"])
