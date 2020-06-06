from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Geo(MPTTModel):
    name = models.CharField(max_length=255, blank=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    lat = models.CharField('Широта', max_length=15, blank=True)
    long = models.CharField('Долгота', max_length=15, blank=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

