from django import forms
from django.core.validators import MaxLengthValidator
from django.forms import Form, ModelForm

from content_sharing.models import Post


class PostForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea({"id": "content-to-be-posted"}))

    class Meta:
        model = Post
        fields = ["content"]


class BioForm(Form):
    bio = forms.CharField(
        widget=forms.Textarea({"id": "bio"}),
        validators=[MaxLengthValidator(600)],
        required=False,
    )
