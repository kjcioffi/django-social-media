from django.urls import path
import user_management.views as views


app_name = 'user_management'
urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
]
