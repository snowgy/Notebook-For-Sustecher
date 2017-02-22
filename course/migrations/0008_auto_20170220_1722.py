# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20170219_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pre',
            field=models.ManyToManyField(null=True, to='course.Pre'),
        ),
        migrations.AlterField(
            model_name='course',
            name='pro',
            field=models.ManyToManyField(null=True, to='course.Pro'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ta',
            name='address',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ta',
            name='reservation',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='reservation',
            field=models.DateTimeField(null=True),
        ),
    ]