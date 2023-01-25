from django import forms
from .models import *

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
