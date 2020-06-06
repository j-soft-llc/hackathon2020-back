from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    
    # TODO: add geo_id

    def get_token(self):
        # token = Token(user=self)
        # token.save()
        # if hasattr(self, 'auth_token'):
        #     result_token = self.auth_token.key
        # else:
        #     token = Token(user=self)
        #     token.save()
        #     print()
        #     print()
        #     print(token)
        #     result_token = token.key
        result_token = 'test'
        return result_token