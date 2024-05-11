from django.urls import path
import user_management.views as views

from django.contrib.auth.views import LoginView


app_name = 'user_management'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='user_management/login.html'), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]
