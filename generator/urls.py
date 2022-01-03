from django.contrib import admin
from django.urls import path, include
from generator.views import *
from django.http import request

app_name = 'generator'
urlpatterns = [
    path('new/', UploadImage.as_view()),
    path('get/', get_result),
    path('/', index)
]