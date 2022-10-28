from django.db import models
from users.models import User
from django.utils import timezone


class Board(models.Model):
    board_name = models.CharField(
        max_length=150,
    )
    created_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        _("created at"),
        default=timezone.now,
        auto_now_add=True,
    )


class Tag(models.Model):
    tag = models.CharField(
        max_length=50,
    )


class BoardTag(models.Model):
    """connect Board & Tag"""

    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
