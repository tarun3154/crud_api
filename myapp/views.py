from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer

class DetailList(generics.RetrieveUpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class CreateList(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class DeleteList(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer