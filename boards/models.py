from django.db import models
from users.models import User
from posts.models import Post
from django.utils import timezone
from django.utils.translation import gettext as _


class Board(models.Model):
    board_name = models.CharField(
        max_length=150,
    )
    created_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        # default=timezone.now,
    )