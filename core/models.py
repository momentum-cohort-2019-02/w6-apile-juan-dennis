from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import get_user_model 
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=true blank=true )
    date_posted = models.DateTimeField('Date Published', auto_now_add=True, null=True)
    date_updated = models.DateTimeField(null=True, auto_now=True)
    votes = models.ManyToManyField(through='Profile', related_name='posts')
    url = models.URLField(max_lenght= 250, null=True)
    # slug = AutoSlugField(unique=True, populate_from="title", blank=True, null=True)



    def __str__(self):
        return self.title


