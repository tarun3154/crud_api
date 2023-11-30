from django.urls import path
from .views import ProductList, ProductDetail, ProductEdit, ProductDelete

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/<int:pk>/edit/', ProductEdit.as_view(), name='product-edit'),
    path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product-delete'),
]
