from django.db import models


class Service(models.Model):
    title = models.CharField('Ваше предложение', max_length=200, null=True)
    description = models.TextField('Подробное описание', null=True)
    price = models.FloatField('Цена услуги', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
