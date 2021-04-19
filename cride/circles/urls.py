"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 10/04/21
@name: urls
"""
from django.conf.urls import url
from django.urls import path

from cride.circles.views import circle_list, circle_create

urlpatterns = [

    path(r'circles/', circle_list, name='circle.list'),
    path(r'circle/create', circle_create, name='circle.create'),
]
