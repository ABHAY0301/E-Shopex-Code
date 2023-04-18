from django.shortcuts import redirect



def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        returnurl = request.META['PATH_INFO']

        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnurl}')

        response = get_response(request)
        return response

    return middleware



# decorator meaning ek fun ke andr ek  fun define krke return krdo