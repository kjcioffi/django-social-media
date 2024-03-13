from django import forms
from django.contrib.auth.forms import UserCreationForm

from user_accounts.models import User

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, help_text='Required.')
    last_name = forms.CharField(max_length=150, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Must provide valid email address')
    birthday = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'birthday')
    