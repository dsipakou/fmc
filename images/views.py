from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from images import serializers
from images.models import Image


class ImageView(APIView):
    serializer_class = serializers.ImageSerializer
    queryset = Image.objects.all()

    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = serializers.ImageSerializer(images, many=True)
        return Response(serializer.data)
