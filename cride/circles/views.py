from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cride.circles.models import Circle
from cride.circles.serializers import CircleSerializer, CreateCircleSerializer


@api_view(['GET'])
def circle_list(request):
    """
    :param request:
    :return:
    """
    circuilos = Circle.objects.filter(is_public=True)
    serializer = CircleSerializer(circuilos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def circle_create(request):
    """

    :param request:
    :return:
    """
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    circle = serializer.save()
    return Response(CircleSerializer(circle).data)
