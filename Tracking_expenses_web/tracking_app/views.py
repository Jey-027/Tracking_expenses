from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Category, Entity, BankProduct, PaymentMethod


# Create your views here.

def home(request):
    return render(request, "tracking_app/home.html")


class CategoryList(ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "tracking_app/list_category.html"


class CreateCategory(CreateView):
    model = Category
    template_name = "tracking_app/create_category.html"
    fields = ('category_name',)
    success_url = "/category/list"


class UpdateCategory(UpdateView):
    model = Category
    template_name = ""
    fields = ('category_name',)


class EntityList(ListView):
    model = Entity
    context_object_name = "entity_list"
    template_name = "tracking_app/list_entity.html"


class CreateEntity(CreateView):
    model = Entity
    template_name = "tracking_app/create_entities.html"
    fields = ('entity_name',)
    success_url = "/entity/list"


class BankProductList(ListView):
    model = BankProduct
    context_object_name = "bank_product_list"
    template_name = "tracking_app/list_bankProduct.html"


class CreateBankProduct(CreateView):
    model = BankProduct
    template_name = "tracking_app/create_bank_product.html"
    fields = ('product_name', 'id_entity',)
    success_url = "/bank_product/list"


class PaymentMethodList(ListView):
    model = PaymentMethod
    context_object_name = "payment_method_list"
    template_name = "tracking_app/list_paymentMethod.html"


class CreatePaymentMethod(CreateView):
    model = PaymentMethod
    template_name = "tracking_app/create_payment_method.html"
    fields = ('method_name',)
    success_url = "/payment_method/list"
