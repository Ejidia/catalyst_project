# Generated by Django 5.2 on 2025-04-24 21:36

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deffered_payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('nin', models.CharField(blank=True, max_length=50, null=True)),
                ('item_bought_on_credit', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default=10, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=10, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('balance', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField(default=datetime.datetime(2025, 4, 25, 0, 36, 47, 323615))),
                ('date_of_payment', models.DateField(default=datetime.datetime(2025, 4, 25, 0, 36, 47, 323615))),
                ('branch', models.CharField(blank=True, max_length=50, null=True)),
                ('agent', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_branch_name', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_type', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_time_of_produce', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('stock_source', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_cost', models.IntegerField(blank=True, default=10, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('total_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('issued_quantity', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(blank=True, max_length=50, null=True)),
                ('seller', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default=10, null=True)),
                ('amount_received', models.IntegerField(blank=True, default=10, null=True)),
                ('issued_to', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=10, null=True)),
                ('date', models.DateField(default=datetime.datetime(2025, 4, 25, 0, 36, 47, 323615))),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karibu.stock')),
            ],
        ),
    ]
