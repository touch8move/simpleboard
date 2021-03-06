# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20160916_0302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='mail',
        ),
        migrations.AlterField(
            model_name='board',
            name='contents',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='hits',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='board',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
