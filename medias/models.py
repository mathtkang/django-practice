from django.db import models
from posts.models import Post


class Attachment(models.Model):
    path = models.TextField(
        primary_key=True,
    )
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
