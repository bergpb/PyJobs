# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-05 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0030_merge_20190703_2238")]

    operations = [
        migrations.AddField(
            model_name="job",
            name="premium_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Data de mudança de Status"
            ),
        )
    ]
