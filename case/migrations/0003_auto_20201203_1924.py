# Generated by Django 2.2 on 2020-12-03 19:24

import case.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20201202_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_content',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='案例内容'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_image',
            field=models.ImageField(default='', null=None, upload_to='case/data/', verbose_name='案例图片'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='案例标题'),
        ),
        migrations.AddField(
            model_name='case',
            name='create_time',
            field=models.DateTimeField(blank=True, default=case.models.create_time, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='case',
            name='image_data',
            field=models.TextField(blank=True, null=True, verbose_name='图片数据'),
        ),
    ]
