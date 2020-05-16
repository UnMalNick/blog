from django.shortcuts import redirect
from datetime import datetime, timedelta


class LimitLectureMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        self.cookie_name = 'jp4ouzjz-cHePrKam_U'
        self.cookie_date_name = 'UMrrfpZfgP46BFhdUZV'
    
    def create_cookie(self, response):
        response.set_cookie(self.cookie_name, 0)
        response.set_cookie(self.cookie_date_name, datetime.now().strftime("%d/%m/%y"))
    
    def delete_cookie(self, response):
        response.delete_cookie(self.cookie_name)
        response.delete_cookie(self.cookie_date_name)
    
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.        

        response = self.get_response(request)

        if not request.user.is_authenticated and request.method == 'GET':
            if 'login' in request.path:
                return response
            
            if request.COOKIES.get(self.cookie_date_name):
                date_str = request.COOKIES.get(self.cookie_date_name)
                limit_date = datetime.strptime(date_str, "%d/%m/%y") + timedelta(days=7)

                if datetime.now() > limit_date:
                    self.create_cookie(response)
                    return response

            if request.COOKIES.get(self.cookie_name):

                value = int(request.COOKIES.get(self.cookie_name))
                
                if value >= 5:
                    return redirect('login')
                
                response.set_cookie(self.cookie_name, value + 1)
            else:
                self.create_cookie(response)
        else:
            if request.COOKIES.get(self.cookie_name):
                self.delete_cookie(response)
        # Code to be executed for each request/response after
        # the view is called.

        return response