from django.urls import path, include
from home.views import HomeView, LogoutView, LoginView, TermsOfServiceView, PrivacyView


urlpatterns = [
    path('',  HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('terminos/', TermsOfServiceView.as_view(), name='ToS'),
    path('privacidad/', PrivacyView.as_view(), name='Privacy'),
]
