from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('category/list', views.CategoryList.as_view(), name="Categories"),
]
