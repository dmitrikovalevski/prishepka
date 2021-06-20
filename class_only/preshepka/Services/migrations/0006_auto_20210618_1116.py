# Generated by Django 3.2.4 on 2021-06-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_service_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1', 'Недвижимость'), ('2', 'Авто и транспорт'), ('3', 'Бытовая техника'), ('4', 'Компьютерная техника'), ('5', 'Телефоны и планшеты'), ('6', 'Электроника'), ('7', 'Женский гардероб'), ('8', 'Мужской гардероб'), ('9', 'Красота и здоровье'), ('10', 'Всё для детей и мам'), ('11', 'Мебель'), ('12', 'Все для дома'), ('13', 'Ремонт и стройка'), ('14', 'Сад и огород'), ('15', 'Хобби, спорт и туризм'), ('16', 'Свадьба и праздники'), ('17', 'Животные'), ('18', 'Бизнес и оборудование'), ('19', 'Работа'), ('20', 'Услуги'), ('21', 'Прочее')], db_index=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Services.rubric'),
        ),
    ]