from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

from post.models import Post
from .models import TermsOfService, Privacy
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


class TermsOfServiceView(View):
    template_name = "home/tos.html"

    def get(self, request):
        terms = TermsOfService.objects.all().order_by('-created_date').last()
        context = {
            'title': 'Terminos de Servicio',
            'terms': terms
        }
        return render(request, self.template_name, context)


class PrivacyView(View):
    template_name = "home/tos.html"

    def get(self, request):
        terms = Privacy.objects.all().order_by('-created_date').last()
        context = {
            'title': 'Politicas de Privacidad',
            'terms': terms
        }
        return render(request, self.template_name, context)