import content_sharing.views as views

from django.urls import path


app_name = 'content_sharing'
urlpatterns = [
    path('', views.index, name='index'),
]