# Generated by Django 3.0.4 on 2020-04-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre(s)')),
                ('last_name', models.CharField(max_length=15, verbose_name='Apellido')),
                ('year', models.CharField(max_length=4, verbose_name='Año de inicio')),
                ('numero_albums', models.IntegerField()),
                ('genero', models.CharField(choices=[('0', 'Pop'), ('1', 'Rock'), ('2', 'Metal'), ('3', 'Electrónica'), ('4', 'Reggaeton'), ('5', 'Baladas'), ('6', 'Regional mexicano'), ('7', 'Banda'), ('8', 'Cumbia'), ('9', 'Salsa'), ('10', 'Alternativa')], max_length=20, verbose_name='Género')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
        ),
    ]
