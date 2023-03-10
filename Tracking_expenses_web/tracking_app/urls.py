from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('list/category', views.CategoryList.as_view(), name="Categories"),
    path('list/entity', views.EntityList.as_view(), name="Entities"),
    path('list/product', views.ProductsList.as_view(), name="Products"),
    path('list/payment_method', views.PaymentMethodList.as_view(), name="PaymentMethods"),
    path('list/monthly_check', views.MonthlyCheckList.as_view(), name="MonthlyCheck"),
    path('create/category', views.CreateCategory.as_view(), name="Create_categories"),
    path('create/entity', views.CreateEntity.as_view(), name="Create_entity"),
    path('create/product', views.CreateProducts.as_view(), name="Create_product"),
    path('create/payment_method', views.CreatePaymentMethod.as_view(), name="Create_paymentMethod"),
    path('create/monthly_check', views.MonthlyCheckCreate.as_view(), name="Create_MonthlyCheck"),
    path('update/category/<pk>', views.UpdateCategory.as_view(), name="Update_category"),
    path('update/entity/<pk>', views.UpdateEntity.as_view(), name="Update_entity"),
    path('update/product/<pk>', views.UpdateProducts.as_view(), name="Update_product"),
    path('update/payment_method/<pk>', views.UpdatePaymentMethod.as_view(), name="Update_paymentProduct"),
    path('update/monthly_check/<pk>', views.MonthlyCheckUpdate.as_view(), name="Update_monthlyCheck"),
]
