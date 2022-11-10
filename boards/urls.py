from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.Boards.as_view()),
    path("<int:id>", views.BoardDetail.as_view()),
    path("<int:board_id>/posts", include("posts.urls")),
]
