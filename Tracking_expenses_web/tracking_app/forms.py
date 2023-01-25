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
