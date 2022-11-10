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


class Tag(models.Model):
    tag = models.CharField(
        max_length=50,
    )


class BoardTag(models.Model):
    """connect Board & Tag"""

    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Attachment(models.Model):
    path = models.TextField(
        primary_key=True,
    )
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(
        _("created at"),
        default=timezone.now,
    )
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment_id = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,  # nullable
    )


class Like(models.Model):
    """connect Post & User"""

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Mark(models.Model):
    """connect Post & User"""

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
