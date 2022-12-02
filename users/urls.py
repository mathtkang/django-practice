from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "users"

urlpatterns = [
    path("", views.Users.as_view()),
    path("signup", views.Signup.as_view()),
    path("login", views.Login.as_view()),
    path("logout", views.Logout.as_view()),
    path("<int:id>/role", views.UserRole.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("token-login", obtain_auth_token),
    path("jwt-login", views.JWTLogin.as_view()),
]
