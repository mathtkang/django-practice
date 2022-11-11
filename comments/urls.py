from django.urls import path
from . import views

app_name = "comments"

# /boards/{board_id}/posts/{post_id}/comments
urlpatterns = [
    path("", views.Comments.as_view()),
    path("<int:id>", views.CommentsDetail.as_view()),
]
