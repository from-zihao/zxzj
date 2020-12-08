# Generated by Django 2.2 on 2020-12-02 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_image', models.ImageField(default='', null=None, upload_to='home/data/', verbose_name='活动展示图片')),
                ('case_image', models.ImageField(default='', null=None, upload_to='home/data/', verbose_name='案例落地图片')),
                ('cooperation_image', models.ImageField(default='', null=None, upload_to='home/data/', verbose_name='合作流程图片')),
                ('activity_image_data', models.TextField(blank=True, null=True, verbose_name='活动展示图片数据')),
                ('case_image_data', models.TextField(blank=True, null=True, verbose_name='案例落地图片数据')),
                ('cooperation_image_data', models.TextField(blank=True, null=True, verbose_name='合作流程图片数据')),
            ],
        ),
    ]
