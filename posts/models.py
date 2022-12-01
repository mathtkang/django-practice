from django.db import models
from django.utils import timezone
from django.conf import settings
from users.models import User
from django.utils.translation import gettext as _


class Post(models.Model):
    title = models.CharField(
        max_length=150,
    )
    content = models.TextField(
        blank=True,
        default="",
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
    )
    written_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board_id = models.ForeignKey("boards.Board", on_delete=models.CASCADE)

class Like(models.Model):
    """connect Post & User"""

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment_id = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,  # nullable
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
    )

class Hashtag(models.Model):
    hashtag = models.CharField(
        max_length=50,
    )
    created_at = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        auto_now=True,
    )

class PostHashTag(models.Model):
    """connect Post & Tag"""

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag_id = models.ForeignKey(Hashtag, on_delete=models.CASCADE)