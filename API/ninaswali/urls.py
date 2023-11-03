#!/usr/bin/python3
from django.urls import path
from .views import *


urlpatterns = [
        path('', Jibu.as_view(), name = 'jibu'),
        ]
