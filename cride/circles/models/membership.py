"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 18/04/21
@name: membership
"""

from django.db import models

from cride.utils.models import CrideModel


class Membership(CrideModel):
    """
        A membership model is that
    """
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    profile = models.ForeignKey(
        "users.Profile",
        on_delete=models.CASCADE,
    )
    circle = models.ForeignKey(
        'circles.Circle',
        on_delete=models.CASCADE,
    )

    is_admin = models.BooleanField(
        'Admin Circle',
        default=False,
    )
    used_invitations = models.PositiveSmallIntegerField(
        default=0,
        help_text='Number of invitations used by member'
    )
    remaining_invitation = models.PositiveSmallIntegerField(
        default=0,
    )
    invited_by = models.ForeignKey(
        'users.User',
        null=True,
        related_name='invited_by',
        on_delete=models.SET_NULL
    )
    # rides
    rides_taken = models.PositiveSmallIntegerField(
        default=0,
    )
    rides_offered = models.PositiveSmallIntegerField(
        default=0
    )
    is_active = models.BooleanField(
        'Active status'
    )

    def __str__(self):
        return "@{} at #{}".format(self.user.username, self.circle)
