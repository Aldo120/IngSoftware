# Generated by Django 3.0.5 on 2020-04-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discos', '0004_auto_20200427_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='titulo',
            field=models.CharField(max_length=40, verbose_name='Titulo'),
        ),
    ]