# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-05 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='课程类别'),
        ),
    ]
