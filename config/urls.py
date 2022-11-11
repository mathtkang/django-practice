from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("boards/", include("boards.urls")),
    path("users/", include("users.urls")),
    path("attachment/", include("medias.urls")),
]
