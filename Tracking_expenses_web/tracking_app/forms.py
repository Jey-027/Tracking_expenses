from django import forms
from .models import *


class MonthlyCheckForm(forms.ModelForm):
    class Meta:
        model = MonthlyCheck

        fields = [
            "id", "date", "id_payment_method", "id_entity", "id_product", "amount", "description", "id_category"
        ]

        widgets = {
            "date": forms.SelectDateWidget,
        }

        labels = {
            "date": "Date",
            "id_payment_method": "Payment method",
            "id_entity": "Entity",
            "id_product": "Product",
            "amount": "Amount",
            "description": "Description".capitalize(),
            "id_category": "Category",
        }

class TransactionControlForm(forms.ModelForm):
    class Meta:
        model = TransactionControl
        fields = [
            "id", "date", "reason", "transaction_value", "payment", "bank_interest", "secure", "observation", "id_financial_product"
        ]

        widgets = {
            "date": forms.SelectDateWidget
        }

        labels = {
            "date": "Date transaction",
            "transaction_value": "Transaction Value",
            "bank_interest": "Bank Interest",
            "id_financial_product": "Financial product",
        }
