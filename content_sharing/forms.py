from django import forms
from django.forms import ModelForm

from content_sharing.models import Post, Profile


class PostForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea({'id': 'content-to-be-posted'}))

    class Meta:
        model = Post
        fields = ['content']

class BioForm(ModelForm):
    bio = forms.CharField(widget=forms.Textarea({'id': 'bio'}))

    class Meta:
        model = Profile
        fields = ['bio']
