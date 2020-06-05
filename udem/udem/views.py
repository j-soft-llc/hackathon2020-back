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
