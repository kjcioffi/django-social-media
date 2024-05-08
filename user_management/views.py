from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render

class RegisterUser(FormView):
    form_class = UserCreationForm
    template_name = 'user_management/register.html'
