# Generated by Django 3.2.5 on 2021-07-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20210720_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='firstapp/photos', verbose_name='Фото'),
        ),
    ]
