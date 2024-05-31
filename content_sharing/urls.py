from django.urls import path

import content_sharing.views as views

app_name = "content_sharing"
urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("api/create_post", views.create_post, name="create_post"),
]
