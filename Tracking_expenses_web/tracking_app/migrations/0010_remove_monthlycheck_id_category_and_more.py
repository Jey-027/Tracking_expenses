# Generated by Django 4.1.4 on 2023-01-10 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_app', '0009_rename_id_bank_product_monthlycheck_id_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlycheck',
            name='id_category',
        ),
        migrations.RemoveField(
            model_name='monthlycheck',
            name='id_entity',
        ),
        migrations.RemoveField(
            model_name='monthlycheck',
            name='id_payment_method',
        ),
        migrations.RemoveField(
            model_name='monthlycheck',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='products',
            name='id_entity',
        ),
        migrations.RemoveField(
            model_name='transactioncontrol',
            name='id_entity',
        ),
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='Entity',
        ),
        migrations.DeleteModel(
            name='MonthlyCheck',
        ),
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='TransactionControl',
        ),
    ]
