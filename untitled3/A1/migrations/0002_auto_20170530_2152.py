# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stream',
            old_name='head_image',
            new_name='head_img',
        ),
        migrations.AlterField(
            model_name='stream',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
