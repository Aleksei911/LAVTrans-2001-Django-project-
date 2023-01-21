from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name='Тема задачи', max_length=50)
    description = models.TextField(verbose_name='Описание')
    add_date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    complete_to = models.DateTimeField(verbose_name='Выполнить до')
    worker = models.ForeignKey('Person', on_delete=models.PROTECT, verbose_name='Сотрудник')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Person(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
