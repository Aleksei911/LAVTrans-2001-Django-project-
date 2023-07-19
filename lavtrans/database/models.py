from django.db import models


# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование собственника')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'


class Car(models.Model):
    number = models.CharField(verbose_name='Номер авто', max_length=10)
    model = models.CharField(verbose_name='Модель ТС', max_length=50, default=None, blank=True, null=True)
    manufacture_year = models.IntegerField(verbose_name='Год выпуска', default=None, blank=True, null=True)
    green_card = models.DateField(verbose_name='Зелёнка', blank=True, null=True)
    strahovka = models.DateField(verbose_name='Страховка', blank=True, null=True)
    tehosmotr = models.DateField(verbose_name='Техосмотр', blank=True, null=True)
    tahograf = models.DateField(verbose_name='Тахограф', blank=True, null=True)
    tamogennoye = models.DateField(verbose_name='Таможенное', blank=True, null=True)
    kasko = models.DateField(verbose_name='КАСКО', blank=True, null=True)
    cmr_strahovka = models.DateField(verbose_name='CMR-страховка', blank=True, null=True)
    e100_rb = models.DateField(verbose_name='Е100 РБ', blank=True, null=True, default=None)
    e100_rf = models.DateField(verbose_name='Е100 РФ', blank=True, null=True, default=None)
    active = models.BooleanField(verbose_name='Отслеживать?', default=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'


class TechPassport(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    vin = models.CharField(max_length=20, verbose_name='VIN')
    type_ts = models.CharField(max_length=75, verbose_name='Тип ТС', blank=True, null=True)
    category = models.CharField(max_length=3, verbose_name='Категория', blank=True, null=True)
    eco_class = models.IntegerField(verbose_name='Эко класс', blank=True, null=True)
    color = models.CharField(max_length=30, verbose_name='Цвет', blank=True, null=True)
    engine_capacity = models.IntegerField(verbose_name='Объем двигателя', blank=True, null=True)
    weight = models.IntegerField(verbose_name='Масса без нагрузки', blank=True, null=True)
    max_weight = models.IntegerField(verbose_name='Максимальная масса', blank=True, null=True)
    manufacturer = models.CharField(max_length=50, verbose_name='Страна производитель', blank=True, null=True)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Стоимость', blank=True, null=True)
    pts = models.CharField(max_length=20, verbose_name='Свидетельство №', blank=True, null=True)
    pts_date = models.DateField(verbose_name='Свидетельство дата', blank=True, null=True)
    place_of_registration = models.CharField(max_length=70, verbose_name='Место регистрации', blank=True, null=True)

    def __str__(self):
        return f'Техпаспорт {self.car}'

    class Meta:
        verbose_name = 'Техпаспорт'
        verbose_name_plural = 'Техпаспорта'


class TechPassportScans(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    scan = models.ImageField(upload_to=f'images/cars/', blank=True, null=True, verbose_name='Сканы документов')

    def __str__(self):
        return f'Сканы документов {self.car}'

    class Meta:
        verbose_name = 'Сканы документов странспортного средства'
        verbose_name_plural = 'Сканы документов странспортных средств'


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


class PassportDriver(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    passport_number = models.CharField(verbose_name='Серия и номер паспорта', max_length=10, blank=True, null=True)
    date_of_issue = models.DateField(verbose_name='Дата выдачи', blank=True, null=True)
    identification_number = models.CharField(max_length=15, verbose_name='Идентификационный номер', blank=True,
                                             null=True)
    authority = models.CharField(max_length=100, verbose_name='Орган, выдавший паспорт', blank=True, null=True)
    place_of_residence = models.CharField(verbose_name='Адрес прописки', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Паспорт {self.driver}'

    class Meta:
        verbose_name = 'Паспорт водителя'
        verbose_name_plural = 'Паспорта водителей'


class DriverScans(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    scan = models.ImageField(upload_to=f'images/drivers/', blank=True, null=True,
                             verbose_name='Сканы документов')

    def __str__(self):
        return f'Сканы документов {self.driver}'

    class Meta:
        verbose_name = 'Сканы документов водителя'
        verbose_name_plural = 'Сканы документов водителей'


class InsuranceEvent(models.Model):
    CALCULATION = 'Калькуляция'
    SERVICE = 'Сервис'

    METHOD = [
        (CALCULATION, 'Калькуляция'),
        (SERVICE, 'Сервис'),
    ]

    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    date_of_submission = models.DateField(verbose_name='Дата подачи в страховую', blank=True, null=True)
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
    image = models.ImageField(upload_to=f'images/insurances/', blank=True, null=True,
                              verbose_name='Фото')

    def __str__(self):
        return f'{self.insurance_event}'

    class Meta:
        verbose_name = 'Фото страхового случая'
        verbose_name_plural = 'Фото страховых случаев'
