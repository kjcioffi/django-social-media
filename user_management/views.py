from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from django.shortcuts import render

from content_sharing.models import Profile

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'user_management/register.html'
    success_url = reverse_lazy('user_management:login')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Create user profile alongside user registration
        Profile.objects.create(user=self.object)

        return response