

from django.db import models


class Base(models.Model):
    created = models.DateTimeField('Data de criação', auto_now_add=True)
    updated = models.DateTimeField('Última atualização', auto_now=True)
    availability = models.BooleanField('Disponibilidade', default=True)

    class Meta:
        abstract = True


class Sign(Base):
    birthday = models.CharField('Aniversário', max_length=100)

    def __str__(self):
        return self.birthday

    class Meta:
        verbose_name = 'Aniversário'
        verbose_name_plural = verbose_name + 's'


class Person(Base):
    name = models.CharField('Nome', max_length=100)
    gender = models.CharField('Gênero', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = verbose_name + 's'
