from django.urls import path
from . import views

urlpatterns = [
    path('create/transaction', views.TransactionControlCreate.as_view(), name="Create_transaction"),
    path('create/financialProduct', views.FinancialProductCreate.as_view(), name="Create_financialProduct"),
    path('list/transaction', views.TransactionControlList.as_view(), name="Transaction_control"),
    path('list/financialProduct', views.FinancialProductList.as_view(), name="fp_list"),
    path('update/financialProduct/<pk>', views.FinancialProductUpdate.as_view(), name="Update_fp"),
    path('update/transaction/<pk>', views.TransactionControlUpdate.as_view(), name="Update_transaction"),
]
