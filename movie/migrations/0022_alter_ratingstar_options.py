# Generated by Django 4.0.5 on 2022-07-08 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0021_remove_usermovierating_user_usermovierating_ip'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
    ]
