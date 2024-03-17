from django import forms
from django.contrib.auth.forms import UserCreationForm

from user_accounts.models import User

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'id': 'first-name'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'id': 'last-name'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'id': 'email'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'id': 'birthday'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'birthday')

    