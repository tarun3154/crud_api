from django.contrib import admin
from .models import *
admin.site.register(Product)



class ProductAdmin(admin.ModelAdmin):
    list_display =('name','price')

    @property
    def display_name_or_price(self):
        if self.name:
            return self.name 
        elif self.price:
            return self.price 
        else:
            return "no name or no price"

    def __str__(self):
        return self.display_name_or_price        