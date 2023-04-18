from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


# create a class for log in
class OrderView(View):
    # self isliye kuki ye is class ka instace method h internal kudh hi call hoga
   # @method_decorator(auth_middleware)  # hm method m direct decorator call nhi kr sakte isliye utlis import krra

    def get(self, request):
        # first indentify the customer
        customer = request.session.get('customer')   # return the customer id
        orders = Order.get_orders_by_customer(customer) # isme ye order h ye model ka h isliye class ka name change kiya iska
        print(orders)
        return render(request, 'orders.html', {'orders' : orders})