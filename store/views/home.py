from django.shortcuts import render , redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        # for removing the quantity
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)   # pop is use for removing the element quantity == 1 isilye kyuki add in cart pe wavis lana h jb item 0 ho jaye to
                    else:
                        cart[product] = quantity - 1   # for removing the quantity of cart
                else:
                    cart[product] = quantity + 1   # coming product id
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')



    def get(self, request):
        cart = request.session.get('cart')
        if not cart:                              #ye isliye krra h kuki jb cart me sab pop ho jaye ga to error ayen gi
            request.session['cart'] = {}

        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category');
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories
        # return HttpResponse('<H1>Abhay</H1>')
        # print("hello")
        print('you are : ', request.session.get('customer_email'))
        return render(request, 'index.html', data)


#def index(request):



