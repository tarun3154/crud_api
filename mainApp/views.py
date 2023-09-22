from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class ListToDo(generics.ListAPIView):
    queryset=ToDo.objects.all()
    serializer_class= todoSerializer

class DetailToDo(generics.RetrieveUpdateAPIView):
    queryset=ToDo.objects.all()
    serializer_class=todoSerializer

class CreateToDo(generics.CreateAPIView):
    queryset=ToDo.objects.all()
    serializer_class=todoSerializer

class DeleteToDo(generics.DestroyAPIView):
    queryset=ToDo.objects.all()
    serializer_class=todoSerializer

    