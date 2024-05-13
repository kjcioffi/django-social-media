from django.forms import ModelForm

from content_sharing.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']