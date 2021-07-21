# Generated by Django 3.2.5 on 2021-07-03 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название пиццы')),
                ('short_description', models.CharField(max_length=30, verbose_name='Краткое описание')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.pizzashop')),
            ],
        ),
    ]
