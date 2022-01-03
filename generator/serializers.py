from rest_framework import serializers
from generator.models import Image


class ImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'gen_type', 'params', 'text_fields')


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'result')
