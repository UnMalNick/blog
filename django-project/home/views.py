from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

from post.models import Post
# Create your views here.


class HomeView(View):
    template_name = 'home/index.html'
    def get(self, request):
        post = Post.objects.filter(is_active=True, is_draft=False)
        context = {
            'posts': post
        }
        return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        logout(request)
        return redirect('home')

class LoginView(View):
    template_name = "session/login.html"
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)