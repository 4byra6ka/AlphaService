from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MainImage(models.Model):
    image = models.ImageField(upload_to='main_image/', verbose_name='Изображение')
    title = models.CharField(max_length=100, verbose_name='Заголовок', **NULLABLE)
    content = models.TextField(verbose_name='Cодержимое', **NULLABLE)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(MainImage, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    archived = models.BooleanField(verbose_name='Архив', default=False)

    def __str__(self):
        return f"{self.pk}: {self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя услуги')
    price = models.PositiveIntegerField(verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE)
    picture = models.ImageField(upload_to='service_image/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    archived = models.BooleanField(verbose_name='Архив', default=False)
    currencyId = models.CharField(max_length=10, verbose_name='Валюта', default='RUR')

    def __str__(self):
        return f"{self.pk}: {self.name}"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Service, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
