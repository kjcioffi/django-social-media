from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from user_accounts.forms import UserSignUpForm

class UserSignUpView(FormView, SuccessMessageMixin):
    template_name = 'user_accounts/sign_up.html'
    form_class = UserSignUpForm
    success_url = reverse_lazy('user_accounts:login')
    success_message = 'Your account was successfully created!'

    def form_valid(self, form):
        form.save()
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return super().form_valid(form)
    
