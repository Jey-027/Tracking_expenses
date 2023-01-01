from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Entity, BankProduct, PaymentMethod


# Create your views here.

def home(request):
    return render(request, "tracking_app/home.html")


class CategoryList(ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "tracking_app/list_category.html"


class EntityList(ListView):
    model = Entity
    context_object_name = "entity_list"
    template_name = "tracking_app/list_entity.html"


class BankProductList(ListView):
    model = BankProduct
    context_object_name = "bank_product_list"
    template_name = "tracking_app/list_bankProduct.html"


class PaymentMethodList(ListView):
    model = PaymentMethod
    context_object_name = "payment_method_list"
    template_name = "tracking_app/list_paymentMethod.html"
