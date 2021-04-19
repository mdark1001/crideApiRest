"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 10/04/21
@name: urls
"""
from django.conf.urls import url
from django.urls import path

from cride.users.views import UserLoginApiView, UserSignupApiView,UserVerifyApiView


urlpatterns = [

    path(r'users/login', UserLoginApiView.as_view(), name='login'),
    path(r'users/singup', UserSignupApiView.as_view(), name='singup'),
    path(r'users/verify', UserVerifyApiView.as_view(), name='singup'),
]
