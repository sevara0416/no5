from django.urls import path
from .views import ProductListAPIView
from . import views

urlpatterns=[
    path("products/",views.ProductListAPIView.as_view(), name="Product-list"),
    path("products/create/",views.ProductCreateAPIView.as_view(), name="Product-create"),
    path("products/<int:pk>/",views.ProductRetrieveAPIView.as_view(), name="Product-detail"),
    path("products/update/<int:pk>/",views.ProductUpdateAPIView.as_view(), name="Product-update"),
    path("products/delete/<int:pk>/",views.ProductDestroyAPIView.as_view(), name="Product-delete"),
    path("products/detail-update/<int:pk>/",views.ProductRetrieveUpdateAPIView.as_view(), name="product-detail-update"),  
    path("products/detail-delete/<int:pk>/",views.ProductRetrieveDestroyAPIView.as_view(), name="product-detail-delete"),
    path("products/<int:pk>/manage/", views.ProductRetrieveUpdateDestroyAPIView.as_view(), name="product-manager"),          
]