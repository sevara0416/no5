from django.urls import path
from .views import ProductListView,ProductDetailView,product_create,product_update,product_delete,RegisterAPIView,ProfileAPIView,LogoutAPIView
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)

urlpatterns=[
    path("products/", ProductListView),
    path("products/create/", product_create),
    path("products/<int:pk>/", ProductDetailView),
    path("products/update/<int:pk>/", product_update),
    path("products/delete/<int:pk>/", product_delete),
    path("register/", RegisterAPIView.as_view()),
    path("profile/", ProfileAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
