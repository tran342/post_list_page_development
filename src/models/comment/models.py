from django.contrib.auth.models import User
from django.db import models

from models.shared.models import TimestampedModel


class Comment(TimestampedModel):
    """
    Post model
    Sample post model
    """
    class Meta:
        db_table = 'content_comment'

    content = models.TextField(null=True, blank=True)
    post = models.ForeignKey('model_post.Post', related_name='post_comments', on_delete=models.CASCADE)
    author = models.ForeignKey('model_author.Author', related_name='author_comments', on_delete=models.CASCADE)
