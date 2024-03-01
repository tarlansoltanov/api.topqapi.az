from django.db import models

from server.apps.core.models import CoreModel


class Worker(CoreModel):
    """Model definition for Worker."""

    name = models.CharField(max_length=255, unique=True)

    class Meta(CoreModel.Meta):
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        """Unicode representation of Worker."""
        return self.name