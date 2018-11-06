from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    photo = serializers.ImageField(read_only=True)