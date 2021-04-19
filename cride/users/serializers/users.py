"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 13/04/21
@name: users
"""
from datetime import timedelta

import jwt as jwt
from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from cride.users.models import User, Profile
from cride.users.models.user import phone_regex


class UserModelSerializer(serializers.ModelSerializer):
    """Model Serializer for user model"""

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name')


class UserLoginSerializer(serializers.Serializer):
    """

    """
    email = serializers.EmailField(

    )
    password = serializers.CharField(
        min_length=8,
    )

    def validate(self, attrs):
        """Check credentials """

        user = authenticate(
            username=attrs['email'],
            password=attrs['password']
        )
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_verified:
            raise serializers.ValidationError("Account is not verified")
        self.context['user'] = user
        return attrs

    def create(self, validated_data):
        """  Generate new token """
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserSingupSerializer(serializers.Serializer):
    """ User signup  Serializer data"""
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    phone_number = serializers.CharField(
        validators=[phone_regex],

    )

    password = serializers.CharField(
        min_length=8,
        max_length=64
    )
    password_confirmation = serializers.CharField(
        min_length=8,
        max_length=64
    )
    first_name = serializers.CharField(
        min_length=2,
        max_length=30
    )
    last_name = serializers.CharField(
        min_length=2,
        max_length=30
    )

    def validate(self, data):
        """

        :param data:
        :return:
        """
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data, is_verified=False)
        Profile.objects.create(user=user)
        self.send_email_verification(user)
        return user

    def send_email_verification(self, user):
        """

        :param user:
        :return:
        """
        token = self.get_verification_token(user)
        subject = "Account Verification"
        from_email = "CRide <noreplay@cride.com>"
        email = render_to_string(
            'emails/users/account_verification.html',
            {
                'token': token,
                'user': user
            }
        )
        msg = EmailMultiAlternatives(subject, email, from_email, [user.email])
        msg.attach_alternative(email, 'text/html')
        msg.send()

    def get_verification_token(self, user):
        """
        :param user:
        :return:
        """
        exp_date = timezone.now() + timedelta(days=3)
        payload = {
            'exp': exp_date.timestamp(),
            'user': user.username,
            'type': 'email_verification',

        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token.decode()


class UserVerifySerializer(serializers.Serializer):
    """"""
    token = serializers.CharField()

    def validate_token(self, attrs):
        """
        :param attrs:
        :return:
        """
        try:
            payload = jwt.decode(attrs, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Token was expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
        if payload['type'] != 'email_verification':
            raise serializers.ValidationError('Invalid token')
        self.context['payload'] = payload
        return attrs

    def save(self):
        """Update user is_verified = True"""
        payload = self.context.get('payload')
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
