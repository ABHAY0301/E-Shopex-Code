from django.views import View
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from store.models.category import Category


#create a class for log in
class Cart(View):
    # self isliye kuki ye is class ka instace method h internal kudh hi call hoga
    def get(self, request):

        categories = Category.get_all_categories()
        check = request.session.get('cart')

        if check is not None:
            ids = list(check.keys())
        else:
            products = Product.get_all_products();
            data = {}
            data['products'] = products
            data['categories'] = categories

            return render(request, 'index.html', data)

        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products' : products } )

