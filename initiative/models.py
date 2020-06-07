import os
import uuid
from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=200, blank=False)
    parent = models.ForeignKey('self', verbose_name='Категория',
                               on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Initiative(models.Model):

    APPEAL = 'appeal'
    COMPLAINT = 'complaint'

    INITIATIVE_TYPES = [
        (APPEAL, 'Обращение'),
        (COMPLAINT, 'Жалоба'),
    ]
    name = models.CharField('Название', max_length=300)
    initiative_text = models.TextField('Текст обращения')
    leader = models.ForeignKey('users.User', related_name='initiative_leader',
                               on_delete=models.SET_NULL, blank=True,
                               null=True)
    category = models.ForeignKey(Category, related_name='initiative_category',
                                 on_delete=models.SET_NULL, blank=True,
                                 null=True)
    initiative_type = models.CharField('Тип', max_length=9, default=APPEAL,
                                       choices=INITIATIVE_TYPES)
    owner = models.ForeignKey('users.User', related_name='initiative_owner',
                              on_delete=models.SET_NULL, null=True)

    @property
    def photo(self):
        return InitiativePhoto.objects.filter(initiative=self)

    # TODO: добавить дополнительные материалы

    def __str__(self):
        return self.initiative_text[:50]


class NamedImageField(models.ImageField):

    def generate_filename(self, instance, filename):
        _, ext = os.path.splitext(filename)
        name = f'{uuid.uuid4().hex}{ext}'
        return super().generate_filename(instance, name)


class InitiativePhoto(models.Model):

    initiative = models.ForeignKey(Initiative, related_name='initiative_photo',
                                   on_delete=models.CASCADE)
    photo = NamedImageField('photo', upload_to='uploads/initiative')
