# Generated by Django 4.1.4 on 2023-01-25 01:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tracking_app', '0014_remove_transactioncontrol_id_financial_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type', models.TextField(choices=[('TC', 'Credit Card'), ('CA', 'Saving Accounts'), ('TD', 'Debit Card'), ('VC', 'Vehicle Loan'), ('INV', 'Investments'), ('OT', 'Others')])),
                ('product_name', models.CharField(max_length=50)),
                ('id_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking_app.entity')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionControl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name=datetime.date)),
                ('reason', models.CharField(max_length=50)),
                ('transaction_value', models.DecimalField(decimal_places=2, default=0, max_digits=15, null=True)),
                ('payment', models.DecimalField(decimal_places=2, default=0, max_digits=15, null=True)),
                ('bank_interest', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('secure', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('observation', models.CharField(blank=True, max_length=100, null=True)),
                ('id_financial_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction_control_app.financialproducts')),
            ],
        ),
    ]
