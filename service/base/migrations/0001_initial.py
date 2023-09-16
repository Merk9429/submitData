# Generated by Django 4.2.2 on 2023-09-16 10:09

import base.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, max_length=9, verbose_name='широта')),
                ('longitude', models.FloatField(blank=True, max_length=9, verbose_name='долгота')),
                ('height', models.IntegerField(blank=True, verbose_name='высота')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('photos', models.ImageField(blank=True, null=True, upload_to=base.models.get_image_path, verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'новый'), ('at_work', 'в работе'), ('accepted', 'принят'), ('rejected', 'отклонен')], default='new', max_length=25)),
                ('beautyTitle', models.CharField(choices=[('the_pass', 'перевал'), ('mountain_peak', 'горная вершина'), ('gorge', 'ущелье'), ('plateau', 'плато')], max_length=50, verbose_name='тип')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='название')),
                ('other_titles', models.CharField(max_length=50, verbose_name='иные названия')),
                ('connect', models.CharField(max_length=250, verbose_name='соединение')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('winter', models.CharField(choices=[('', 'не указано'), ('1A', '1a'), ('1B', '1б'), ('2А', '2а'), ('2В', '2б'), ('3А', '3а'), ('3В', '3б')], max_length=2, verbose_name='зима')),
                ('summer', models.CharField(choices=[('', 'не указано'), ('1A', '1a'), ('1B', '1б'), ('2А', '2а'), ('2В', '2б'), ('3А', '3а'), ('3В', '3б')], max_length=2, verbose_name='лето')),
                ('autumn', models.CharField(choices=[('', 'не указано'), ('1A', '1a'), ('1B', '1б'), ('2А', '2а'), ('2В', '2б'), ('3А', '3а'), ('3В', '3б')], max_length=2, verbose_name='осень')),
                ('spring', models.CharField(choices=[('', 'не указано'), ('1A', '1a'), ('1B', '1б'), ('2А', '2а'), ('2В', '2б'), ('3А', '3а'), ('3В', '3б')], max_length=2, verbose_name='весна')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parent', models.IntegerField(blank=True)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('phone', models.CharField(max_length=15, verbose_name='телефон')),
                ('name', models.CharField(max_length=30, verbose_name='имя')),
                ('surname', models.CharField(max_length=30, verbose_name='фамилия')),
                ('patronymic', models.CharField(max_length=30, verbose_name='отчество')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.images')),
                ('point', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.perevaladded')),
            ],
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.users'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='coord_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.coords'),
        ),
    ]
