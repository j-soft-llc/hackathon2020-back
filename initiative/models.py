from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(models.Model):
    name = models.CharField('Название', max_length=200, blank=False)
    parent = models.ForeignKey('self', verbose_name='Категория', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Geo(MPTTModel):
    name = models.CharField(max_length=255, blank=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = 'Область'
        verbose_name_plural = 'Области'
