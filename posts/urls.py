from django.urls import path, include
from . import views

app_name = "posts"

# /boards/{board-id}/posts/
urlpatterns = [
    path("", views.Posts.as_view()),
    path("<int:id>", views.PostsDetail.as_view()),
    path("<int:id>/like", views.PostsLike.as_view()),
    path("<int:id>/comments/", include("comments.urls")),
]
