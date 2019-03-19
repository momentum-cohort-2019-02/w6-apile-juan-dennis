from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# Comments belong to a user, the author, and a post.
# Users have many posts, comments, and votes.

User = get_user_model()


class Comment(models.Model):
    user_comment = models.TextField(null=True, blank=True)

    commenter = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.PROTECT,
    )
