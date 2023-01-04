from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('category/list', views.CategoryList.as_view(), name="Categories"),
    path('entity/list', views.EntityList.as_view(), name="Entities"),
    path('bank_product/list', views.BankProductList.as_view(), name="Bank_Products"),
    path('payment_method/list', views.PaymentMethodList.as_view(), name="PaymentMethods"),
    path('category/create', views.CreateCategory.as_view(), name="Create_categories"),
    path('entity/create', views.CreateEntity.as_view(), name="Create_entity"),
    path('bank_product/create', views.CreateBankProduct.as_view(), name="Create_bankProduct"),
    path('payment_method/create', views.CreatePaymentMethod.as_view(), name="Create_paymentMethod"),
    path('category/update/<pk>', views.UpdateCategory.as_view(), name="Update_category"),
    path('entity/update/<pk>', views.UpdateEntity.as_view(), name="Update_entity"),
    path('bank_product/update/<pk>', views.UpdateBankProduct.as_view(), name="Update_bankProduct"),
    path('payment_method/update/<pk>', views.UpdatePaymentMethod.as_view(), name="Update_paymentProduct"),
]
