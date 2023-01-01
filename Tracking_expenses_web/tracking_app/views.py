from django.shortcuts import render
from django.views.generic import ListView
from .models import Category


# Create your views here.

def home(request):
    return render(request, "tracking_app/home.html")


class CategoryList(ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "tracking_app/list_category.html"
