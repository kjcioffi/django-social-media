from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from django.shortcuts import render

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'user_management/register.html'
    success_url = reverse_lazy('user_management:register')
