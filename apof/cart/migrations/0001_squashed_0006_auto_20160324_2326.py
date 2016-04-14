# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 12:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('cart', '0001_initial'), ('cart', '0002_auto_20160324_1621'), ('cart', '0003_auto_20160324_1935'), ('cart', '0004_auto_20160324_2247'), ('cart', '0005_auto_20160324_2305'), ('cart', '0006_auto_20160324_2326')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0007_auto_20160320_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Size')),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]