# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-04 01:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0008_host_host_fail_hostgroup_ipsource'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oraclecluster',
            options={'verbose_name': 'Oracle_cluster', 'verbose_name_plural': 'Oracle_cluster'},
        ),
    ]