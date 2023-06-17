from django.db import models


# Create your models here.
class Car(models.Model):
    number = models.CharField(verbose_name='Номер авто', max_length=10)
    green_card = models.DateField(verbose_name='Зелёнка', blank=True, null=True)
    strahovka = models.DateField(verbose_name='Страховка', blank=True, null=True)
    tehosmotr = models.DateField(verbose_name='Техосмотр', blank=True, null=True)
    tahograf = models.DateField(verbose_name='Тахограф', blank=True, null=True)
    tamogennoye = models.DateField(verbose_name='Таможенное', blank=True, null=True)
    kasko = models.DateField(verbose_name='КАСКО', blank=True, null=True)
    cmr_strahovka = models.DateField(verbose_name='CMR-страховка', blank=True, null=True)
    active = models.BooleanField(verbose_name='Отслеживать?', default=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'


class Driver(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=20)
    name = models.CharField(verbose_name='Имя', max_length=20)
    middle_name = models.CharField(verbose_name='Отчество', max_length=20)
    passport = models.DateField(verbose_name='Паспорт')
    visa = models.DateField(verbose_name='Виза', blank=True, null=True)
    driver_card = models.DateField(verbose_name='Водительское удостоверение')
    active = models.BooleanField(verbose_name='Отслеживать?', default=True)

    def __str__(self):
        return f'{self.last_name} {self.name} {self.middle_name}'

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
