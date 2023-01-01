from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('category/list', views.CategoryList.as_view(), name="Categories"),
    path('entity/list', views.EntityList.as_view(), name="Entities"),
    path('bank_product/list', views.BankProductList.as_view(), name="Bank Products"),
    path('payment_method/list', views.PaymentMethodList.as_view(), name="PaymentMethods"),
]
