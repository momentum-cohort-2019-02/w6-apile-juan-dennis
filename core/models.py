from django.db import models
from django.contrib.auth.models import get_user_model

# Create your models here.
# Comments belong to a user, the author, and a post.
# Users have many posts, comments, and votes.

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Comment(models.Model):
    user_comment = models.TextField(null=True, blank=True)
    time_of_comment = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        to=Post, related_name="comments", on_delete=models.CASCADE)
    vote = models.ManyToManyField(through="profile", related_name="comments")
    author = models.ForeignKey(
        Profile,
        related_name="comments",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.user_comment


# votes are many to many