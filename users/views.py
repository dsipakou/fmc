from rest_framework.views import APIView

from users import serializers
from users.models import User


class UserView(APIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()