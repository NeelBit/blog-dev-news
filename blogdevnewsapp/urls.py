from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home, acerca_de, contacto, registro, login_view

#app_name = "blogdevnews"

urlpatterns = [
    path('', home, name='home'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('acerca-de/', acerca_de, name='acerca-de'),
    path('contacto/', contacto, name='contacto'),
]