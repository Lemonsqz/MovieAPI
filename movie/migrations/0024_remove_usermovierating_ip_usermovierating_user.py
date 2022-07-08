# Generated by Django 4.0.5 on 2022-07-08 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0023_alter_ratingstar_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermovierating',
            name='ip',
        ),
        migrations.AddField(
            model_name='usermovierating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]