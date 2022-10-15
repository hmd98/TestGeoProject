# Generated by Django 4.1.2 on 2022-10-15 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tsys', '0007_remove_allnodes_road_allnodes_road'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allnodes',
            name='road',
        ),
        migrations.AddField(
            model_name='allnodes',
            name='road',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Tsys.roads'),
        ),
    ]
