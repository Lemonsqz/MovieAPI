# Generated by Django 4.0.5 on 2022-07-04 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_alter_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
