import jsonfield
from django.db import models

from scraping.utils import from_cyrillic_to_english


def default_urls():
    return {"cian": "", "m_2": ""}


class City(models.Model):
    objects = None
    name = models.CharField(max_length=50,
                            verbose_name='Название города',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Название городов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_english(str(self.name))
        super().save(*args, **kwargs)


class Metro(models.Model):
    objects = None
    name = models.CharField(max_length=50,
                            verbose_name='Станция метро',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_english(str(self.name))
        super().save(*args, **kwargs)


class Declaration(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок объявления')
    residential_complex = models.CharField(max_length=250, verbose_name='Название ЖК')
    description = models.TextField(verbose_name='Описание объявления')
    city = models.ForeignKey('city', on_delete=models.CASCADE,
                             verbose_name='Город')
    metro = models.ForeignKey('metro', on_delete=models.CASCADE,
                              verbose_name='Метро')
    timestamp = models.DateField(auto_now_add=True)
    price = models.CharField(max_length=250, verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class Error(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    data = jsonfield.JSONField()


class Url(models.Model):
    objects = None
    city = models.ForeignKey('city', on_delete=models.CASCADE,
                             verbose_name='Город')
    metro = models.ForeignKey('metro', on_delete=models.CASCADE,
                              verbose_name='Метро')
    url_data = jsonfield.JSONField(default=default_urls)
    
    class Meta:
        unique_together = ("city", "metro")
