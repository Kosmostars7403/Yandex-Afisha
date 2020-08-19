from django.db import models
from django.conf import settings
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(max_length=400, verbose_name='Краткое описание', blank=True)
    description_long = HTMLField(blank=True)
    lng = models.FloatField(verbose_name='Координаты: долгота')
    lat = models.FloatField(verbose_name='Координаты: широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place_images",
                              verbose_name='Место')
    file = models.ImageField(upload_to='places_images', verbose_name='Файл изображения')
    position = models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')

    def __str__(self):
        return '{} {}'.format(self.position, self.place)

    class Meta(object):
        ordering = ['position']
