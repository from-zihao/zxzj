# Generated by Django 2.2 on 2020-12-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubmitinfo',
            name='contact_content',
            field=models.TextField(blank=True, null=True, verbose_name='联系内容'),
        ),
    ]
