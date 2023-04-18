from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

#create a class for log in
class Login(View):
    # self isliye kuki ye is class ka instace method h internal kudh hi call hoga

    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')       #for holding the url for orders page
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                #request.session['customer_email'] = customer.email   id unique hoti h isliye mail ki jrurt nhi h
                #return redirect('homepage')  this change into below
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)  #/ kisi url pe jana chate h to redirect use nhi krte  uske lye httpresponse
                else:
                    Login.return_url = None
                    return redirect('homepage') # agr name hi help se redirect krna h to  ye use hota h

            else:
                error_message = 'Email or Password Invalid !!'
        else:
            error_message = 'Email or Password Invalid !!'

        print(email, password)

        return render(request, 'login.html', {'error': error_message})  # kuki error code m asi  h login page m


def logout(request):
    request.session.clear()
    return redirect('login')