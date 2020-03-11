from django.shortcuts import render
from .models import Customers,Products,Orders
def home(request):
    customers = Customers.objects.all()
    products = Products.objects.all()
    orders =  Orders.objects.all()
    total_orders = len(orders)
    delivery_orders = orders.filter(status='Delivered').count()
    pending_orders = orders.filter(status='Pending').count()
    outfordelivery_orders = orders.filter(status='Outfordelivery').count()

    context = {
        'customers':customers,
        'orders':orders,
        'products':products,
        'total_orders':total_orders,
        'delivery_orders':delivery_orders,
        'pending_orders':pending_orders,
        'outfordelivery_orders':outfordelivery_orders
    }

    return render(request, 'accounts/dashboard.html',context)

def products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'accounts/products.html',context)

def orders(request):
    return render(request, 'accounts/orders.html')
def customer(request,pk):
    customer = Customers.objects.get(id=pk)
    context = {'customer':customer}
    return render(request,'accounts/customer.html',context)
def all_customers(request):
    customers = Customers.objects.all()
    context = {'customers':customers}
    return render(request,'accounts/customers.html',context)