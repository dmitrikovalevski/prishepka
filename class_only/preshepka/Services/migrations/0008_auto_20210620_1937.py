# Generated by Django 3.2.4 on 2021-06-20 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0007_alter_rubric_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='rubric',
        ),
        migrations.DeleteModel(
            name='Rubric',
        ),
    ]
