from django.db import models

class Web(models.Model):
    image = models.ImageField(upload_to='web/images/',null=True, blank=True,verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Blog(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True,verbose_name='Имя')
    text = models.TextField(null=True, blank=True,verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Дата отзыва')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-name']


    def __str__(self):
        return self.name
