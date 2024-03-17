from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from user_accounts.forms import UserSignUpForm

class UserSignUpView(FormView):
    template_name = 'user_accounts/sign_up.html'
    form_class = UserSignUpForm

    # TO-DO: re-direct to 'login view' when it's implemented
    success_url = reverse_lazy('user_accounts:sign-up') 

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
