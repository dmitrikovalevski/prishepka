# Generated by Django 3.2.4 on 2021-06-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_auto_20210618_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(choices=[('Недвижимость', 'Недвижимость'), ('Авто и транспорт', 'Авто и транспорт'), ('Бытовая техника', 'Бытовая техника'), ('Компьютерная техника', 'Компьютерная техника'), ('Телефоны и планшеты', 'Телефоны и планшеты'), ('Электроника', 'Электроника'), ('Женский гардероб', 'Женский гардероб'), ('Мужской гардероб', 'Мужской гардероб'), ('Красота и здоровье', 'Красота и здоровье'), ('Всё для детей и мам', 'Всё для детей и мам'), ('Мебель', 'Мебель'), ('Все для дома', 'Все для дома'), ('Ремонт и стройка', 'Ремонт и стройка'), ('Сад и огород', 'Сад и огород'), ('Хобби, спорт и туризм', 'Хобби, спорт и туризм'), ('Свадьба и праздники', 'Свадьба и праздники'), ('Животные', 'Животные'), ('Бизнес и оборудование', 'Бизнес и оборудование'), ('Работа', 'Работа'), ('Услуги', 'Услуги'), ('Прочее', 'Прочее')], db_index=True, max_length=30),
        ),
    ]
