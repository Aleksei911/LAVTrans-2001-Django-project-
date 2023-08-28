from django.db import models
from database.models import Car, Driver


# Create your models here.
class Delivery(models.Model):
    lavtrans = 'ЧТУП ЛАВТранс-2001'
    lavtrans_rus = 'ООО ЛАВТРАНС-2001 РУС'
    multilane = 'ООО МУЛЬТИЛАЙН'
    clk = 'SIA CLK'

    EUR = 'EUR'
    BYN = 'BYN'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY = [
        (EUR, 'EUR'),
        (BYN, 'BYN'),
        (USD, 'USD'),
        (RUB, 'RUB'),
    ]

    TRANSPORTER = [
        (lavtrans, 'ЧТУП ЛАВТранс-2001'),
        (lavtrans_rus, 'ООО ЛАВТРАНС-2001 РУС'),
        (multilane, 'ООО МУЛЬТИЛАЙН'),
        (clk, 'SIA CLK'),
    ]

    date_of_delivery = models.DateField(verbose_name='Дата загрузки')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_delivery_set')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver_delivery_set')
    transporter = models.CharField(max_length=25, choices=TRANSPORTER, verbose_name='Перевозчик')
    next_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='next_car_delivery_set')
    next_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='next_driver_delivery_set')
    next_transporter = models.CharField(max_length=25, choices=TRANSPORTER, verbose_name='Последующий перевозчик',
                                        blank=True, null=True)
    waybill_number = models.CharField(max_length=5, verbose_name='Номер путевого листа', null=True, blank=True)
    waybill_date = models.DateField(verbose_name='Дата путевого листа', null=True, blank=True)
    customer = models.CharField(max_length=50, verbose_name='Заказчик', null=True, blank=True)
    customer_contact = models.CharField(max_length=255, verbose_name='Контактное лицо', null=True, blank=True)
    application_number = models.CharField(max_length=15, verbose_name='Номер заявки', null=True, blank=True)
    application_date = models.DateField(verbose_name='Дата заявки', null=True, blank=True)
    route = models.TextField(verbose_name='МАРШРУТ (ЗАГРУЗКА -ТАМОЖНИ +ДОВОЗ)', null=True, blank=True)
    rate = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Ставка', blank=True, null=True)
    rate_currency = models.CharField(max_length=4, choices=CURRENCY, verbose_name='Денежная единица для ставки',
                                     blank=True, null=True)
    liters = models.IntegerField(verbose_name='Количество литров топлива продано', blank=True, null=True)
    liters_amount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True,
                                        verbose_name='Получили за топливо (EUR)')
    storage = models.IntegerField(verbose_name='Выезд из накопителя (EUR)', blank=True, null=True)
    customs_clearance = models.DecimalField(max_digits=11, decimal_places=2,
                                            verbose_name='Стоимость таможенного оформления', blank=True, null=True)
    customs_currency = models.CharField(max_length=4, choices=CURRENCY, blank=True, null=True,
                                        verbose_name='Денежная единица для таможенного оформления')
    electronic_seal = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True,
                                          verbose_name='Стоимость электронной пломбы (BYN)')
    prostoi = models.IntegerField(verbose_name='Количество дней простоя', blank=True, null=True)
    rate_for_prostoi = models.IntegerField(verbose_name='Ставка за день простоя', blank=True, null=True)
    prostoi_currency = models.CharField(max_length=4, choices=CURRENCY, verbose_name='Денежная единица для простоя',
                                        blank=True, null=True)
    score_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Номер счёта')
    score_date = models.DateField(verbose_name='Дата выставления счёта', null=True, blank=True)
    score_total = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True, default=None,
                                      verbose_name='Итоговая сумма счёта')
    score_currency = models.CharField(max_length=4, choices=CURRENCY, verbose_name='Денежная единица для счёта',
                                      blank=True, null=True)
    payment_term = models.IntegerField(verbose_name="Срок оплаты (Банковских дней)", blank=True, null=True)

    def __str__(self):
        return f"{self.date_of_delivery} - {self.car}"

    class Meta:
        verbose_name = 'Перевозка'
        verbose_name_plural = 'Перевозки'


class DeliveryBack(models.Model):
    EUR = 'EUR'
    BYN = 'BYN'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY = [
        (EUR, 'EUR'),
        (BYN, 'BYN'),
        (USD, 'USD'),
        (RUB, 'RUB'),
    ]

    delivery = models.ForeignKey('Delivery', on_delete=models.CASCADE, null=True, blank=True)
    date_of_back_delivery = models.DateField(verbose_name='Дата загрузки', null=True, blank=True)
    back_customer = models.CharField(max_length=50, verbose_name='Заказчик', null=True, blank=True)
    back_customer_contact = models.CharField(max_length=255, verbose_name='Контактное лицо', null=True, blank=True)
    back_application_number = models.CharField(max_length=15, verbose_name='Номер заявки', null=True, blank=True)
    back_application_date = models.DateField(verbose_name='Дата заявки', null=True, blank=True)
    back_route = models.TextField(verbose_name='МАРШРУТ', null=True, blank=True)
    back_rate = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Ставка', blank=True, null=True)
    back_rate_currency = models.CharField(max_length=4, choices=CURRENCY, verbose_name='Денежная единица для ставки',
                                     blank=True, null=True)
    back_prostoi = models.IntegerField(verbose_name='Количество дней простоя', blank=True, null=True)
    back_rate_for_prostoi = models.IntegerField(verbose_name='Ставка за день простоя', blank=True, null=True)
    back_prostoi_currency = models.CharField(max_length=4, choices=CURRENCY, verbose_name='Денежная единица для простоя',
                                        blank=True, null=True)
    back_score_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Номер счёта')
    back_score_date = models.DateField(verbose_name='Дата выставления счёта', null=True, blank=True)
    back_score_total = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True, default=None,
                                      verbose_name='Итоговая сумма счёта')
    back_score_currency = models.CharField(max_length=4, choices=CURRENCY, verbose_name='Денежная единица для счёта',
                                           blank=True, null=True)
    back_payment_term = models.IntegerField(verbose_name="Срок оплаты (Банковских дней)", blank=True, null=True)

    def __str__(self):
        return f"{self.date_of_back_delivery} - {self.back_customer}"

    class Meta:
        verbose_name = 'Обратка'
        verbose_name_plural = 'Обратки'
