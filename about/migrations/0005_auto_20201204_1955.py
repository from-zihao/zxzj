# Generated by Django 2.2 on 2020-12-04 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20201204_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='titile_image_data',
            new_name='title_image_data',
        ),
    ]