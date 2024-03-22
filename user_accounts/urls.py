from django.urls import path

from django.contrib.auth.views import LoginView
from user_accounts.views import UserSignUpView

app_name = 'user_accounts'

urlpatterns = [
    path('sign-up/', UserSignUpView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(template_name='user_accounts/login.html'), name='login'),
]