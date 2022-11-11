from django.urls import path, include
from . import views

app_name = "boards"

# /boards
urlpatterns = [
    path("", views.Boards.as_view()),
    path("<int:id>", views.BoardDetail.as_view()),
    path("<int:id>/posts/", include("posts.urls")),
]
