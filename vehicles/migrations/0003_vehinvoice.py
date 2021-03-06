# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehworkinvoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inv_No', models.CharField(max_length=25, verbose_name='Invoice No')),
                ('Inv_Date', models.DateField(verbose_name='Invoice Date')),
                ('Inv_Customer_Name', models.CharField(max_length=30, verbose_name='Customer Name')),
                ('Inv_Customer_Contact', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact No')),
                ('Inv_Price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Inv_Order_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.VehWorkOrder', verbose_name='Work Order No')),
            ],
        ),
    ]
