from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .forms import *


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
    success_url = "/list/category"


class UpdateCategory(UpdateView):
    model = Category
    template_name = "tracking_app/update_category.html"
    fields = ('category_name',)
    success_url = "/list/category"


class EntityList(ListView):
    model = Entity
    context_object_name = "entity_list"
    template_name = "tracking_app/list_entity.html"


class CreateEntity(CreateView):
    model = Entity
    template_name = "tracking_app/create_entities.html"
    fields = ('entity_name',)
    success_url = "/list/entity"


class UpdateEntity(UpdateView):
    model = Entity
    template_name = "tracking_app/update_entity.html"
    fields = ('entity_name',)
    success_url = "/list/entity"


class ProductsList(ListView):
    model = Products
    context_object_name = "product_list"
    template_name = "tracking_app/list_Products.html"


class CreateProducts(CreateView):
    model = Products
    template_name = "tracking_app/create_product.html"
    fields = ('product_name', 'id_entity',)
    success_url = "/list/product"


class UpdateProducts(UpdateView):
    model = Products
    template_name = "tracking_app/update_Products.html"
    fields = ('product_name', 'id_entity',)
    success_url = "/list/product"


class PaymentMethodList(ListView):
    model = PaymentMethod
    context_object_name = "payment_method_list"
    template_name = "tracking_app/list_paymentMethod.html"


class CreatePaymentMethod(CreateView):
    model = PaymentMethod
    template_name = "tracking_app/create_payment_method.html"
    fields = ('method_name',)
    success_url = "/list/payment_method"


class UpdatePaymentMethod(UpdateView):
    model = PaymentMethod
    template_name = "tracking_app/update_paymentMethod.html"
    fields = ('method_name',)
    success_url = "/list/payment_method"


class MonthlyCheckList(ListView):
    model = MonthlyCheck
    context_object_name = "monthly_check_list"
    template_name = "tracking_app/list_monthly_check.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_amount = MonthlyCheck.objects.aggregate(total_amount=Sum('amount'))["total_amount"]
        total_entity = MonthlyCheck.objects.filter(id_payment_method=1).aggregate(total_entity=Sum('amount'))["total_entity"]
        total_product = MonthlyCheck.objects.filter(id_payment_method=5).aggregate(total_product=Sum('amount'))["total_product"]
        total_cash = MonthlyCheck.objects.filter(id_payment_method=4).aggregate(total_cash=Sum('amount'))["total_cash"]

        context["TotalAmount"] = total_amount
        context["TotalEntity"] = total_entity
        context["TotalProduct"] = total_product
        context["TotalCash"] = total_cash
        return context


class MonthlyCheckCreate(CreateView):
    model = MonthlyCheck
    template_name = "tracking_app/create_record_mc.html"
    form_class = MonthlyCheckForm
    success_url = "/list/monthly_check"


class MonthlyCheckUpdate(UpdateView):
    model = MonthlyCheck
    template_name = "tracking_app/update_record_mc.html"
    fields = "__all__"
    success_url = "/list/monthly_check"
