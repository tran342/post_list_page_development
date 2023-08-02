from django.contrib.auth.models import User
from django.db import models

from models.shared.models import TimestampedModel


class Author(TimestampedModel):
    """
    Author model
    1-1 for User model to content author's information
    """
    class Meta:
        db_table = 'content_author'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True)
    # And other information relates to the author
