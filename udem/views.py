from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


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
        if user_type == 'user':
            user_data = settings.SIMPLE_USER
        else:
            user_data = settings.LEADER_USER

        user = User.objects.filter(username=user_data['login']).first()
        if not user:
            user = User.objects.create_user(username=user_data['login'], email=user_data['email'])

        if hasattr(user, 'auth_token'):
            result_token = user.auth_token.key
        else:
            token = Token(user=user)
            token.save()
            result_token = token.key
        return Response({'token': result_token})
