from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=150,
    )
    content = models.TextField(
        blank=True,
        default="",
    )
    written_user_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    board_id = models.ForeignKey("boards.Board", on_delete=models.CASCADE)
