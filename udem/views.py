from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User


class Ping(APIView):

    def get(self, request, *args, **kwargs):
        """
        Проверка API:

        Если бэкенд работает, вернет

            {
                "result": "ping"
            }
        """
        return Response({'result': 'ping'})


class GetTokenByUser(APIView):

    def get(self, request, *args, **kwargs):
        user_type = kwargs.get('type')
        user_types_data = {
            'user' : settings.SIMPLE_USER,
            'leader' : settings.LEADER_USER
        }
        user_data = user_types_data.get(user_type, settings.LEADER_USER)

        user = User.objects.filter(username=user_data['login']).first()
        if not user:
            user = User.objects.create_user(username=user_data['login'], email=user_data['email'])
        
        return Response({'token': user.get_token()})
