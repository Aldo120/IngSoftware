# Generated by Django 3.0.5 on 2020-04-27 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artista', '0002_auto_20200427_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20, verbose_name='Titulo')),
                ('duracion', models.TimeField()),
                ('lista_canciones', models.TextField()),
                ('year', models.CharField(max_length=4, verbose_name='Año publicación')),
                ('portada', models.ImageField(blank=True, null=True, upload_to='discos')),
                ('precio', models.FloatField()),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artista.Artista')),
            ],
            options={
                'ordering': ['titulo', 'artista'],
            },
        ),
    ]
