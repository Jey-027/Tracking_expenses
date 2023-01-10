from django import forms
from .models import MonthlyCheck


class MonthlyCheckForm(forms.ModelForm):
    class Meta:
        model = MonthlyCheck

        fields = [
            "id", "date", "id_payment_method", "id_entity", "id_bank_product", "amount", "description", "id_category"
        ]

        widgets = {
            "date": forms.SelectDateWidget,
        }

        labels = {
            "date": "Date",
            "id_payment_method": "Payment method",
            "id_entity": "Entity",
            "id_bank_product": "Bank Product",
            "amount": "Amount",
            "description": "Description".capitalize(),
            "id_category": "Category",
        }
