"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 13/04/21
@name: login
"""
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from cride.users.serializers.users import UserLoginSerializer, UserModelSerializer, UserSingupSerializer, \
    UserVerifySerializer


class UserLoginApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserSignupApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSingupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserVerifyApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': 'Account was verified. Thanks'
        }
        return Response(data, status=status.HTTP_200_OK)
