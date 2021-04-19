"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 09/04/21
@name: user
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from cride.utils.models import CrideModel

phone_regex = RegexValidator(
    regex=r'\+?1?\d{9,15}$',
    message='Phone number has not format required'
)


class User(CrideModel, AbstractUser):
    """
    Custom Class for users, this class add extra info to user base django
    """
    email = models.EmailField(
        'Email Address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'Client Status',
        default=True,
        help_text=""""""
    )
    is_verified = models.BooleanField(
        'User verified',
        default=False,
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
