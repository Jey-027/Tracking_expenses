from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .forms import *

class TransactionControlList(ListView):
    model = TransactionControl
    context_object_name = "transaction_list"
    template_name = "transaction_control_app/list_transaction.html"


class TransactionControlCreate(CreateView):
    model = TransactionControl
    template_name = "transaction_control_app/create_transaction.html"
    form_class = TransactionControlForm
    success_url = "/list/transaction"


class TransactionControlUpdate(UpdateView):
    model = TransactionControl
    template_name = "transaction_control_app/update_transaction.html"
    form_class = TransactionControlForm
    success_url = "/list/transaction"


class FinancialProductList(ListView):
    model = FinancialProducts
    context_object_name = "financialP_list"
    template_name = "transaction_control_app/list_financial_product.html"


class FinancialProductCreate(CreateView):
    model = FinancialProducts
    template_name = "transaction_control_app/create_financial_product.html"
    fields = "__all__"
    success_url = "/list/financialProduct"


class FinancialProductUpdate(UpdateView):
    model = FinancialProducts
    template_name = "transaction_control_app/update_fp.html"
    fields = "__all__"
    success_url = "/list/financialProduct"
