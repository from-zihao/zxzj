# Generated by Django 2.2 on 2020-12-04 19:46

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201202_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='create_time',
            field=models.DateTimeField(blank=True, default=home.models.create_time, null=True, verbose_name='创建时间'),
        ),
    ]
