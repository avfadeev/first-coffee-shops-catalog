# Generated by Django 3.2.5 on 2021-07-03 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_pizza'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name': 'Пицца', 'verbose_name_plural': 'Пиццы'},
        ),
        migrations.AlterModelOptions(
            name='pizzashop',
            options={'verbose_name': 'Пиццерия', 'verbose_name_plural': 'Пиццерии'},
        ),
    ]