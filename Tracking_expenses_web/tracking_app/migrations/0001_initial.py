# Generated by Django 4.1.4 on 2022-12-31 01:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('entity_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_method',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('method_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Monthly_check',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name=datetime.date)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.CharField(max_length=50)),
                ('id_bank_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking_app.bank_product')),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking_app.category')),
                ('id_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking_app.entity')),
                ('id_payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking_app.payment_method')),
            ],
        ),
        migrations.AddField(
            model_name='bank_product',
            name='id_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking_app.entity'),
        ),
    ]
