# Generated by Django 2.2 on 2020-04-07 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200405_1846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
