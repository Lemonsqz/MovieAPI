# Generated by Django 4.0.5 on 2022-06-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_comment_options_comment_active_comment_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, max_length=100, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=70, verbose_name='Ваше имя'),
        ),
    ]