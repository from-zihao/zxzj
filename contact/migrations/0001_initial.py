# Generated by Django 2.2 on 2020-12-04 20:24

import contact.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.CharField(blank=True, max_length=255, null=True, verbose_name='经度')),
                ('lat', models.CharField(blank=True, max_length=255, null=True, verbose_name='纬度')),
                ('create_time', models.DateTimeField(blank=True, default=contact.models.create_time, null=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '公司坐标',
                'verbose_name_plural': '公司坐标',
            },
        ),
        migrations.CreateModel(
            name='UserSubmitInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='客户名')),
                ('contact_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='联系方式')),
                ('create_time', models.DateTimeField(blank=True, default=contact.models.create_time, null=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '客户提交信息',
                'verbose_name_plural': '客户提交信息',
            },
        ),
    ]
