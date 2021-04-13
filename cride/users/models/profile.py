"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 09/04/21
@name: profile
"""
from cride.utils.models import CrideModel
from django.db import models


class Profile(CrideModel):
    """

    """
    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE
    )

    picture = models.ImageField(
        'Picture',
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    biography = models.TextField(
        null=True,
        max_length=500,
    )
    rides_token = models.PositiveIntegerField(
        default=0
    )
    rides_offered = models.PositiveIntegerField(
        default=0
    )
    reputacion = models.FloatField(
        default=5.0,
        help_text=''
    )

    def __str__(self):
        return str(self.user)
