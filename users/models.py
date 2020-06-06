from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from initiative.models import Category
from geo.models import Geo


class User(AbstractUser):

    avatar_link = models.URLField('Аватар', max_length=200,
                                  blank=True, null=True)
    vk_id = models.CharField('Id Вк', max_length=50,
                             blank=True, null=True)
    instagram_id = models.CharField('Id Instagram', max_length=50,
                                    blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    second_name = models.CharField('Фамилия', max_length=50,
                                   blank=True, null=True)
    middle_name = models.CharField('Отчество', max_length=50,
                                   blank=True, null=True)
    age = models.PositiveSmallIntegerField('Возраст', blank=True, null=True)
    profession = models.CharField('Проффессия', max_length=200,
                                  blank=True, null=True)
    address = models.ForeignKey(Geo, related_name='address_geo',
                                on_delete=models.SET_NULL, blank=True,
                                null=True)
    district = models.ForeignKey(Geo, related_name='district_geo',
                                 on_delete=models.SET_NULL, blank=True,
                                 null=True)
    сompetencies = models.ManyToManyField(Category, related_name='categories')

    @property
    def is_leader(self):
        return self.district is not None

    @property
    def vote_count(self):
        return self.leader_vote.all().count()

    def get_token(self):
        if hasattr(self, 'auth_token'):
            result_token = self.auth_token.key
        else:
            token = Token(user=self)
            token.save()
            result_token = token.key
        return result_token

    def get_vote_initiatives(self):
        initiatives = [vote.initiative for vote in self.initiative_vote_user.all()]
        return initiatives

    def get_leaders(self):
        leaders = [vote.leader for vote in self.leader_vote_user.all()]
        return leaders

    def get_users(self):
        users = [vote.user for vote in self.leader_vote.all()]
        return users

# TODO: Добавить дополнительные адреса
# class UserAddresses(models.Model):
