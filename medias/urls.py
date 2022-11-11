from django.urls import path
from . import views

app_name = "medias"

# /attachment
urlpatterns = [
    path("", views.Medias.as_view()),
]
