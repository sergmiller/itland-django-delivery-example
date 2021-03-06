# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', models.CharField(max_length=50)),
                ('max_cost', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('from_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_edge_index', models.IntegerField()),
                ('edges', models.ManyToManyField(to='delivery.Edge')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfEdge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('max_weight', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Route'),
        ),
        migrations.AddField(
            model_name='order',
            name='to_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Location'),
        ),
        migrations.AddField(
            model_name='edge',
            name='edge_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.TypeOfEdge'),
        ),
        migrations.AddField(
            model_name='edge',
            name='end_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Location'),
        ),
        migrations.AddField(
            model_name='edge',
            name='start_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Location'),
        ),
        migrations.AddField(
            model_name='deliverybase',
            name='orders',
            field=models.ManyToManyField(to='delivery.Order'),
        ),
    ]
