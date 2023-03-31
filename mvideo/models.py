from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='сотрудник', on_delete=models.SET_NULL, **NULLABLE)
    email = models.EmailField(verbose_name='E-mail')
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house = models.PositiveIntegerField(verbose_name='номер дома', **NULLABLE)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='сотрудник', on_delete=models.SET_NULL, **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='название продукта')
    model = models.CharField(max_length=100, verbose_name='модель', **NULLABLE)
    date = models.DateField(verbose_name='Дата выхода')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Supplier(models.Model):
    FACTORY = 'FACTORY'
    RETAIL = 'RETAIL'
    ENTREPRENEUR = 'ENTREPRENEUR'

    SUPPLY_CHAIN = (
        (FACTORY, 'Завод'),
        (RETAIL, 'Розничная сеть'),
        (ENTREPRENEUR, 'Индивидуальный предприниматель')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='сотрудник', on_delete=models.SET_NULL, **NULLABLE)
    level = models.CharField(max_length=50, choices=SUPPLY_CHAIN)
    title = models.CharField(max_length=150, verbose_name='название')
    contact = models.ForeignKey('mvideo.Contact', on_delete=models.SET_NULL, verbose_name='контакты', **NULLABLE)
    product = models.ForeignKey('mvideo.Product', on_delete=models.SET_NULL, verbose_name='продукты', **NULLABLE)
    chain = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='задолженность', **NULLABLE)
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.title
