from rest_framework.response import Response
from rest_framework.views import APIView

from users import serializers
from users.models import User


class UserView(APIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)