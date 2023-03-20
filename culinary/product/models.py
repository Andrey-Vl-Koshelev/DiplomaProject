from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True,verbose_name='Заголовок')
    name = models.CharField(max_length=200, null=True, blank=True,verbose_name='Название')
    date = models.DateField(verbose_name='Дата')
    image = models.ImageField(upload_to='web/images/',verbose_name='Фото')
    new_price = models.IntegerField(default=0, null=True, blank=True,verbose_name='Новая цена')
    old_price = models.IntegerField(default=0, null=True, blank=True,verbose_name='Старая цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-name']

    def __str__(self):
        return self.name
