# Generated by Django 4.1.2 on 2022-10-15 14:07

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tsys', '0005_allnodes_road'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roads',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326, unique=True),
        ),
    ]
