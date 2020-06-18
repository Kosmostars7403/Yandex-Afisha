from django.db import models
from django.conf import settings

class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(max_length=400, verbose_name='Краткое описание', blank=True)
    description_long = models.TextField(verbose_name='Полное описание', blank=True)
    lng = models.FloatField(verbose_name='Координаты: долгота')
    lat = models.FloatField(verbose_name='Координаты: широта')

    def __str__(self):
        return self.title

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='places_images')
    position = models.PositiveSmallIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return '{} {}'.format(self.position, self.place)


    def get_absolute_image_url(self):
        return self.file.url

    class Meta(object):
        ordering = ['position']
