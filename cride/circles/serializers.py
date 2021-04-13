"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 10/04/21
@name: serializers
"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from cride.circles.models import Circle


class CircleSerializer(serializers.Serializer):
    """

    """
    name = serializers.CharField()
    slug = serializers.SlugField()
    description = serializers.CharField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()


class CreateCircleSerializer(serializers.Serializer):
    """"""
    name = serializers.CharField(
        max_length=150,
    )
    slug = serializers.SlugField(
        max_length=40,
        validators=[
            UniqueValidator(queryset=Circle.objects.all())
        ]
    )
    description = serializers.CharField(
        allow_blank=True,
        allow_null=True
    )
    is_public = serializers.BooleanField(
        default=True
    )

    def create(self, validated_data):
        return Circle.objects.create(**validated_data)
