from django.db import models

# Create your models here.
models
from django.db import models
from datetime import date

# Create your models here.

# payment method table
class Payment_method(models.Model):
    id = models.AutoField(primary_key=True)
    method_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id,self.method_name}"

# Entity table
class Entity(models.Model):
    id = models.AutoField(primary_key=True)
    entity_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id, self.entity_name}"

# Bank product table
class Bank_product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    id_entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id, self.product_name, self.id_entity}"

# Category table
class category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id, self.category_name}"

#Monthly check table 
class Monthly_check(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(date)
    id_payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE)
    id_entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    id_bank_product = models.ForeignKey(Bank_product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=50)
    id_category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id, self.date, self.id_payment_method, self.id_entity, self.id_bank_product, self.amount, self.description, self.id_category}"





