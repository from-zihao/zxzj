# Generated by Django 2.2 on 2020-12-07 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=255, verbose_name='资讯标题')),
                ('news_content', models.CharField(max_length=255, verbose_name='资讯内容')),
                ('news_image', models.ImageField(default='', null=None, upload_to='news/data/', verbose_name='资讯图片')),
                ('news_file', models.FileField(default='', null=None, upload_to='news/data/', verbose_name='资讯文件')),
                ('image_data', models.TextField(blank=True, null=True, verbose_name='图片数据')),
                ('create_time', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 7, 19, 6, 19, 679443), null=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '资讯',
                'verbose_name_plural': '资讯',
            },
        ),
    ]
