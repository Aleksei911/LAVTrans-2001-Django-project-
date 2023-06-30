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


class InsuranceEvent(models.Model):
    CALCULATION = 'Калькуляция'
    SERVICE = 'Сервис'

    METHOD = [
        (CALCULATION, 'Калькуляция'),
        (SERVICE, 'Сервис'),
    ]

    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    date_of_submission = models.DateField(verbose_name='Дата подачи в страховую')
    polis_number = models.CharField(max_length=10, verbose_name='Страховой полис')
    police_sertificate = models.BooleanField(verbose_name='Справка с ГАИ?', default=False)
    repair_method = models.CharField(max_length=13, choices=METHOD, verbose_name='Способ ремонта', blank=True,
                                     null=True)
    calculation_sum = models.DecimalField(max_digits=20, decimal_places=2,
                                          verbose_name='Страховая насчитала по калькуляции',
                                          blank=True, null=True)
    expenses = models.DecimalField(max_digits=20, decimal_places=2,
                                   verbose_name='Наши расходы по восстановлению (Калькуляция)', blank=True, null=True)
    margin = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='В нашу пользу (Калькуляция)',
                                 default=0)
    service_name = models.CharField(max_length=50, verbose_name='На какой сервис отправили ТС', blank=True, null=True)
    service_date = models.DateField(verbose_name='Дата отправки на сервис', blank=True, null=True)
    service_sum = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Сумма счета от сервиса',
                                      blank=True, null=True)
    final_docs = models.DateField(verbose_name='Дата передачи документов по ремонту в страховую', blank=True, null=True)
    payment_date = models.DateField(verbose_name='Дата оплаты от страховой', blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.car} {self.driver}'

    class Meta:
        verbose_name = 'Страховой случай'
        verbose_name_plural = 'Страховые случаи'

    def save(self, *args, **kwargs):
        calculation = self.calculation_sum
        expenses = self.expenses
        if calculation and expenses:
            self.margin = calculation - expenses
        else:
            self.margin = 0
        super(InsuranceEvent, self).save(*args, **kwargs)


class ImagesInsuranceEvent(models.Model):
    insurance_event = models.ForeignKey('InsuranceEvent', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return f'{self.insurance_event}'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
