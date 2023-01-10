from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('category/list', views.CategoryList.as_view(), name="Categories"),
    path('entity/list', views.EntityList.as_view(), name="Entities"),
    path('product/list', views.ProductsList.as_view(), name="Products"),
    path('payment_method/list', views.PaymentMethodList.as_view(), name="PaymentMethods"),
    path('monthly_check/list', views.MonthlyCheckList.as_view(), name="MonthlyCheck"),
    path('transaction/list', views.TransactionControlList.as_view(), name="Transaction_control"),
    path('financialProduct/list', views.FinancialProductList.as_view(), name="fp_list"),
    path('category/create', views.CreateCategory.as_view(), name="Create_categories"),
    path('entity/create', views.CreateEntity.as_view(), name="Create_entity"),
    path('product/create', views.CreateProducts.as_view(), name="Create_product"),
    path('payment_method/create', views.CreatePaymentMethod.as_view(), name="Create_paymentMethod"),
    path('monthly_check/create', views.MonthlyCheckCreate.as_view(), name="Create_MonthlyCheck"),
    path('transaction/create', views.TransactionControlCreate.as_view(), name="Create_transaction"),
    path('financialProduct/create', views.FinancialProductCreate.as_view(), name="Create_financialProduct"),
    path('category/update/<pk>', views.UpdateCategory.as_view(), name="Update_category"),
    path('entity/update/<pk>', views.UpdateEntity.as_view(), name="Update_entity"),
    path('product/update/<pk>', views.UpdateProducts.as_view(), name="Update_product"),
    path('payment_method/update/<pk>', views.UpdatePaymentMethod.as_view(), name="Update_paymentProduct"),
    path('monthly_check/update/<pk>', views.MonthlyCheckUpdate.as_view(), name="Update_monthlyCheck"),
]
