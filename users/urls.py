from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("signup", views.Signup.as_view()),
    path("login", views.Login.as_view()),
    path("logout", views.Logout.as_view()),
    path("<int:id>/role", views.UserRole.as_view()),
    path("change-password", views.ChangePassword.as_view()),
]
