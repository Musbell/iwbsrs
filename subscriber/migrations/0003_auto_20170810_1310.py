# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-10 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0002_captureimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captureimage',
            name='model_pic',
            field=models.ImageField(default='media/None/no-img.jpg', upload_to='media/'),
        ),
    ]
