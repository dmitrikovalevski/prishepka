from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    picture = models.ImageField(upload_to='service', null=True, blank=True)
    title = models.CharField(max_length=200,)
    descriptions = models.TextField()
    price = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(default=0)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Comments(models.Model):
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment


class Rubric(models.Model):
    RUBRICS = [
        ('Недвижимость', 'Недвижимость'),
        ('Авто и транспорт', 'Авто и транспорт'),
        ('Бытовая техника', 'Бытовая техника'),
        ('Компьютерная техника', 'Компьютерная техника'),
        ('Телефоны и планшеты', 'Телефоны и планшеты'),
        ('Электроника', 'Электроника'),
        ('Женский гардероб', 'Женский гардероб'),
        ('Мужской гардероб', 'Мужской гардероб'),
        ('Красота и здоровье', 'Красота и здоровье'),
        ('Всё для детей и мам', 'Всё для детей и мам'),
        ('Мебель', 'Мебель'),
        ('Все для дома', 'Все для дома'),
        ('Ремонт и стройка', 'Ремонт и стройка'),
        ('Сад и огород', 'Сад и огород'),
        ('Хобби, спорт и туризм', 'Хобби, спорт и туризм'),
        ('Свадьба и праздники', 'Свадьба и праздники'),
        ('Животные', 'Животные'),
        ('Бизнес и оборудование', 'Бизнес и оборудование'),
        ('Работа', 'Работа'),
        ('Услуги', 'Услуги'),
        ('Прочее', 'Прочее'),
    ]
    name = models.CharField(max_length=30, db_index=True, choices=RUBRICS)

    def __str__(self):
        return self.name
