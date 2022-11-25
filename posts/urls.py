from django.urls import path  # , include
from . import views

app_name = "posts"

# /posts
urlpatterns = [
    path("", views.Posts.as_view()),
    path("<int:id>", views.PostDetail.as_view()),
    path("<int:post_id>/like", views.PostLike.as_view()),
    path("<int:post_id>/comments", views.PostComments.as_view()),
    path("<int:post_id>/comments/<int:comment_id>", views.PostCommentDetail.as_view()),
]