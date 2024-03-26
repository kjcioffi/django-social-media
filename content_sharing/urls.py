from django.urls import path
from .views import *

app_name = 'content_sharing'
urlpatterns = [
    path('', homepage, name='home_page'),
]
