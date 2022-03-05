from django.db import models
from django.utils import timezone


class ModelBase(models.Model):
    created_at = models.DateTimeField(editable=True, blank=True, null=True)
    updated_at = models.DateTimeField(editable=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        if not self.updated_at:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        get_latest_by = 'created_at'
