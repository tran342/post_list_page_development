from django.db import models
from django.utils import timezone


# First, define the Manager subclass.
class TimestampedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    valid_objects = TimestampedManager()
    objects = models.Manager()
