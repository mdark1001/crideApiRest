"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 09/04/21
@name: models
"""
from django.db import models


class CrideModel(models.Model):
    """
        Class models base  for mdoels in this project
    """

    created = models.DateTimeField(
        auto_now_add=True,
        help_text=''
    )
    updated = models.DateTimeField(
        auto_now=True,
        help_text=''
    )

    class Meta:
        abstract = True
        ordering = ['-created', '-updated']
        get_latest_by = 'created'
