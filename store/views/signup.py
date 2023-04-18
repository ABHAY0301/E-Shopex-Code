from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


# create a class for signup
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation
        # creating a dictionary for reload page to save the feild

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name, last_name=last_name,
                            phone=phone, email=email,
                            password=password)

        # hold the error message
        error_message = self.validateCustomer(customer)

        # saving

        if not error_message:
            print(first_name, last_name, phone, email, password)
            # hashing the password
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    # function for validate a customer
    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = "First name must be 2 char long or more"
        elif not customer.last_name:
            error_message = "Last Name Required !!"
        elif len(customer.last_name) < 4:
            error_message = "Last name must be 2 char long or more"
        elif not customer.phone:
            error_message = "Phone number required !!"
        elif len(customer.phone) < 10:
            error_message = "Phone number must be 10 digit"
        elif not customer.password:
            error_message = "Password required !!"
        elif len(customer.password) < 7:
            error_message = "Password must be 2 char long or more"
        elif customer.isExists():
            error_message = 'Email Address Already Registered !!'

        return error_message
