from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Client(AbstractUser):
    is_seller = models.BooleanField(default=False, verbose_name='Является продавцом')

    class Meta:
        verbose_name = 'Никнейм клиента'
        verbose_name_plural = 'Никнеймы клиентов'
        ordering = ['date_joined']

    def __str__(self):
        return self.username


class Color(models.Model):
    shade = models.CharField(max_length=255, verbose_name='Оттенок')

    class Meta:
        verbose_name = 'Возможный оттенок цветов'
        verbose_name_plural = 'Возможные оттенки цветов'
        ordering = ['shade']

    def __str__(self):
        return self.shade


class Lot(models.Model):
    seller = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='lots', verbose_name='Продавец')
    flower_type = models.CharField(max_length=255, verbose_name='Тип цветов')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Оттенок')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price_per_item = models.FloatField(verbose_name='Цена за 1 цветок(р.)')
    is_visible = models.BooleanField(default=True, verbose_name='Видимость для покупателей')

    class Meta:
        verbose_name = 'Лот товара'
        verbose_name_plural = 'Лоты товаров'
        ordering = ['seller']

    def __str__(self):
        return f'{self.seller}, {self.flower_type}, {self.color}'


class Comment(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупатель')
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, verbose_name='Лот покупки')
    text = models.TextField(verbose_name='Текст комментария')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_date']

    def __str__(self):
        return self.text


class Order(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, verbose_name='Лот покупки')
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупатель')
    quantity = models.PositiveIntegerField(verbose_name='Количество купленных цветов')


    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ['buyer']

    def __str__(self):
        return self.lot.seller.username
