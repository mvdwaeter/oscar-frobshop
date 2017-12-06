# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-06 20:51
from __future__ import unicode_literals

from django.db import migrations


def create_product_class(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    ProductClass = apps.get_model('catalogue', 'ProductClass')
    ProductClass.objects.create(
        name='Digital Content',
        slug='digital-content',
        requires_shipping=False,
        track_stock=False,
    )


def create_partner(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Partner = apps.get_model('partner', 'Partner')
    Partner.objects.create(
        name='Pie Mall Co'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
        # Oscar apps
        ('catalogue', '0001_initial'),
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_product_class),
        migrations.RunPython(create_partner),
    ]
