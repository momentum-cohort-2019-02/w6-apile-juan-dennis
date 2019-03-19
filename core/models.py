from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
# Comments belong to a user, the author, and a post.
# Users have many posts, comments, and votes.

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(
        'Date Published', auto_now_add=True, null=True)
    date_updated = models.DateTimeField(null=True, auto_now=True)
    votes = models.ManyToManyField(to='Profile', related_name='posts')
    url = models.URLField(max_length=250, null=True)

    # slug = AutoSlugField(unique=True, populate_from="title", blank=True, null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Comment(models.Model):
    user_comment = models.TextField(null=True, blank=True)
    time_of_comment = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        Post, related_name="comments_post", on_delete=models.CASCADE)
    vote = models.ManyToManyField(to="Profile", related_name="comments_vote")
    author = models.ForeignKey(
        Profile,
        related_name="comments_author",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.user_comment


# votes are many to many
