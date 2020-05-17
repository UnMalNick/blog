from django.shortcuts import redirect
from datetime import datetime, timedelta


class LimitLectureMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        self.cookie_name = 'jp4ouzjz'
        self.cookie_date_name = 'UMrrfpZfgP46BFhdUZV'
        
        self.GOOGLE_BOT_USER_AGENTS = [
            'APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)',
            'Mediapartners-Google',
            'Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)',
            'AdsBot-Google (+http://www.google.com/adsbot.html)',
            'Googlebot-Image/1.0',
            'Googlebot-News',
            'Googlebot-Video/1.0',
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z‡ Safari/537.36',
            'Googlebot/2.1 (+http://www.google.com/bot.html)',
            'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z‡ Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'AdsBot-Google-Mobile-Apps',
            'FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 (compatible; Google-Read-Aloud; +https://support.google.com/webmasters/answer/1061943)',
            'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012; DuplexWeb-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/49.0.2623.75 Safari/537.36 Google Favicon',
        ]
    
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

        if request.headers.get('User-Agent') in self.GOOGLE_BOT_USER_AGENTS:
            return response

        if not request.user.is_authenticated and request.method == 'GET':
            if 'login' in request.path:
                return response
            
            if request.COOKIES.get(self.cookie_date_name):
                date_str = request.COOKIES.get(self.cookie_date_name)
                limit_date = datetime.strptime(date_str, "%d/%m/%y") + timedelta(days=30)

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