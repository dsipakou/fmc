from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

