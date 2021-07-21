from django.db import models


# Create your models here.

class CoffeeShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Кофейня')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Интернет-адрес кофейни')

    class Meta:
        verbose_name = 'Кофейня'
        verbose_name_plural = 'Кофейни'

    def __str__(self):
        return self.name


class Coffee(models.Model):
    coffeeshop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название кофе')
    short_description = models.CharField(max_length=30, verbose_name='Краткое описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    photo = models.ImageField('Фото', upload_to='firstapp/photos', default='', blank=True)

    class Meta:
        verbose_name = 'Кофе'
        verbose_name_plural = 'Кофе'
        ordering = ['name']

    def __str__(self):
        return self.name


class Order(models.Model):
    coffee = models.ForeignKey(Coffee, verbose_name="Кофе", on_delete=models.CASCADE)
    name = models.CharField(max_length=32, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")