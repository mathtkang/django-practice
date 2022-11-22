from django.urls import path  # , include
from . import views


app_name = "posts"

# /posts
urlpatterns = [
    path("", views.Posts.as_view()),
    path("<int:id>", views.PostDetail.as_view()),
    path("<int:id>/like", views.PostLike.as_view()),
]
