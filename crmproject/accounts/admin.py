from django.contrib import admin
from .models import Products,Customers,Orders
class AdminCustomers(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','mobile','location']
# class AdminProducts(admin.ModelAdmin):
#     list_display = ['name','price','description']

admin.site.register(Customers,AdminCustomers)
admin.site.register(Products)
admin.site.register(Orders)
