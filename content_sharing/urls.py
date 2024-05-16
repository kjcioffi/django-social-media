import content_sharing.views as views

from django.urls import path


app_name = 'content_sharing'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/create_post', views.create_post, name='create_post'),
]