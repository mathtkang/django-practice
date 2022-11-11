from django.db import models
from users.models import User
from posts.models import Post
from django.utils import timezone
from django.utils.translation import gettext as _


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
