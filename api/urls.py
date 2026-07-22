from django.urls import path
from .views import ProductListView,ProductDetailView,product_create,product_update,product_delete
from . import views

urlpatterns=[
    path("products/", ProductListView),
    path("products/create/", product_create),
    path("products/<int:pk>/", ProductDetailView),
    path("products/update/<int:pk>/", product_update),
    path("products/delete/<int:pk>/", product_delete),
]
