from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("boards/", include("boards.urls")),
    path("posts/", include("posts.urls")),
    path("attachment/", include("medias.urls")),
    path("users/", include("users.urls")),
]
