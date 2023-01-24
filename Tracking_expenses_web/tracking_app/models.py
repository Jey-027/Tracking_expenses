# Create your models here.
from django.db import models
from datetime import date


# Create your models here.

# payment method table
class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    method_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.method_name}"


# Entity table
class Entity(models.Model):
    id = models.AutoField(primary_key=True)
    entity_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.entity_name}"


# Bank product table
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    id_entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name}"


# Category table
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category_name}"


# Monthly check table
class MonthlyCheck(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(date)
    id_payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    id_entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=50)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id, self.date, self.id_payment_method, self.id_entity, self.id_product, self.amount, self.description, self.id_category}"


class FinancialProducts(models.Model):
    product_type_choices = [
        ("TC", "Credit Card"), ("CA", "Saving Accounts"), ("TD", "Debit Card"), ("VC", "Vehicle Loan"),
        ("INV", "Investments"), ("OT", "Others")
    ]
    id = models.AutoField(primary_key=True)
    product_type = models.TextField(choices=product_type_choices)
    product_name = models.CharField(max_length=50)
    id_entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.product_type} - " + f"{self.id_entity} - " + f"{self.product_name}"
 
class TransactionControl(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(date)
    reason = models.CharField(max_length=50)
    transaction_value = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=True)
    payment = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=True)
    bank_interest = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    secure = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    observation = models.CharField(max_length=100, blank=True, null=True)
    id_financial_product = models.ForeignKey(FinancialProducts, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id, self.date, self.reason ,self.transaction_value, self.payment, self.bank_interest, self.secure, self.observation, self.id_financial_product}"
