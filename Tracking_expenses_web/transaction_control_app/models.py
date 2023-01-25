from django.db import models
from tracking_app.models import Entity
from datetime import date

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
        return f"{self.id, self.date, self.reason, self.transaction_value, self.payment, self.bank_interest, self.secure, self.observation, self.id_financial_product}"
