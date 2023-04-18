from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order


# create a class for log in
class CheckOut(View):
    # self isliye kuki ye is class ka instace method h internal kudh hi call hoga
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        try:
            customer_obj = Customer.objects.get(id=customer)
        except Customer.DoesNotExist:
            # handle the case when the customer does not exist
            # for example, redirect the user to log in page
            return render(request, 'login.html')

        cart = request.session.get('cart')  # is vali cart m quantities h

        # cart.keys se product ki ids mil jayegi then id pass krke ssare product mil jaye ge

        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:


            order = Order(customer=customer_obj,
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))  # str isliye kuki number or str se compare nhi kr sakte

            #customer.save()
            order.save()



        # after order place we have to clear the session ka cart or session ek dict h
        request.session['cart'] = {}

        return redirect('cart')
