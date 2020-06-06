from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from initiative.models import Geo


class User(AbstractUser):

    avatar_link = models.URLField('Аватар', max_length=200, blank=True, null=True)
    vk_id = models.CharField('Id Вк', max_length=50, blank=True, null=True)
    instagram_id = models.CharField('Id Instagram', max_length=50, blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    second_name = models.CharField('Фамилия', max_length=50, blank=True, null=True)
    middle_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    age = models.PositiveSmallIntegerField('Возраст', blank=True, null=True)
    profession = models.CharField('Проффессия', max_length=200, blank=True, null=True)
    address = models.ForeignKey(Geo, related_name='address_geo', on_delete=models.SET_NULL, blank=True, null=True)

    # TODO: add Competencies and geo

    def get_token(self):
        # token = Token(user=self)
        # token.save()
        if hasattr(self, 'auth_token'):
            result_token = self.auth_token.key
        else:
            token = Token(user=self)
            token.save()
            print()
            print()
            print(token)
            result_token = token.key
        # result_token = 'test'
        return result_token

# TODO: Добавить дополнительные адреса 
# class UserAddresses(models.Model):

    