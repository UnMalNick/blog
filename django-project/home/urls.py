from django.urls import path, include
from home.views import HomeView, LogoutView, LoginView


urlpatterns = [
    path('',  HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
]
