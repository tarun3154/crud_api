from django.urls import path
from .views import *

urlpatterns = [
    path('',ProductList.as_view()),
    path('<int:pk>/',DetailList.as_view()),
    path('create',CreateList.as_view()),
    path('delete/<int:pk>',DeleteList.as_view())
]

