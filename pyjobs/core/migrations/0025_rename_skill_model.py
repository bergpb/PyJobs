# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-17 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("core", "0024_jobapplication_created_at")]

    operations = [migrations.RenameModel(old_name="Skills", new_name="Skill")]
