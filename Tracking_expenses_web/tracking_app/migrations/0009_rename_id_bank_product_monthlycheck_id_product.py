# Generated by Django 4.1.4 on 2023-01-10 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_app', '0008_rename_bankproduct_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlycheck',
            old_name='id_bank_product',
            new_name='id_product',
        ),
    ]