from django.db import models


class Type(models.Model):
    name = models.CharField(verbose_name='Типы задач', max_length=100)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время изменения', auto_now=True)

    def __str__(self):
        return self.name