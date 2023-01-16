from django.db import models


# Create your models here.
class Car(models.Model):
    number = models.CharField(verbose_name='Номер авто', max_length=10)
    tehosmotr = models.DateField(verbose_name='Техосмотр')
    strahovka = models.DateField(verbose_name='Страховка')
    tamogennoye = models.DateField(verbose_name='Таможенное')
    tahograf = models.DateField(verbose_name='Тахограф')
    active = models.BooleanField(verbose_name='Отслеживать?', default=True)

    def __str__(self):
        return self.number


class Driver(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=20)
    last_name = models.CharField(verbose_name='Фамилия', max_length=20)
    passport = models.DateField(verbose_name='Паспорт')
    visa = models.DateField(verbose_name='Виза')
    driver_card = models.DateField(verbose_name='Водительское удостоверение')
    active = models.BooleanField(verbose_name='Отслеживать?', default=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'
