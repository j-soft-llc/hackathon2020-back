from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=200, blank=False)
    parent = models.ForeignKey('self', verbose_name='Категория', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
