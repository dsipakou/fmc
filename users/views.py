from rest_framework.views import APIView

from users.models import User


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
