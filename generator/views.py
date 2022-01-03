from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from generator.serializers import *
from datetime import datetime


class UploadImage(generics.CreateAPIView):
    serializer_class = ImageDetailSerializer


class UploadImageView(generics.ListAPIView):
    serializer_class = ImageListSerializer
    queryset = Image.objects.all()


def get_result(request):
    idd = request.GET['id']
    image = Image.objects.get(pk=int(idd))
    image.action()
    file_name = f"{image.gen_type}_{datetime.now().strftime('%H-%M_%d-%m')}.png"
    response = HttpResponse(image.result, content_type="image/png")
    response['Content-Disposition'] = f'inline; filename={file_name}'
    return response


def index(request):
    return render(request, 'index.html', {})
