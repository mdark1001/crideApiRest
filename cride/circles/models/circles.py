"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 10/04/21
@name: circles
"""
from cride.utils.models import CrideModel
from django.db import models


class Circle(CrideModel):
    """

    """
    name = models.CharField(
        max_length=150,
    )
    slug = models.SlugField(
        unique=True,
        max_length=40,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    picture = models.ImageField(
        upload_to='circles/pictures',
        blank=True,
        null=True
    )
    rides_offered = models.PositiveIntegerField(
        default=0
    )
    rides_taken = models.PositiveIntegerField(
        default=0
    )
    is_verified = models.BooleanField(
        default=False,
        help_text='Circle is a official group'
    )
    is_public = models.BooleanField(
        help_text='Circle is checked as public',
        default=False
    )
    is_limited = models.BooleanField(
        default=False,
        help_text='Check if a circle has limited number of members',
    )
    member_limited = models.PositiveIntegerField(
        default=0,
        help_text='Number of members',
    )

    def __str__(self):
        return self.name

    class Meta(CrideModel.Meta):
        ordering = ['-rides_taken', '-rides_taken']
