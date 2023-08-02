from django.contrib.auth.models import User
from django.db import models

from models.shared.models import TimestampedModel


class Post(TimestampedModel):
    """
    Post model
    Sample post model
    """
    class Meta:
        db_table = 'content_post'

    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey('model_author.Author', related_name='author_posts', on_delete=models.CASCADE)
