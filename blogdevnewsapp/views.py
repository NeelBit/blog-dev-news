from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'blogdevnewsapp/home.html')

def acerca_de(request):
    return render(request, 'blogdevnewsapp/acerca-de.html')

def contacto(request):
    return render(request, 'blogdevnewsapp/contacto.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio después de iniciar sesión
        else:
            return render(request, 'blogdevnewsapp/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'blogdevnewsapp/login.html')

def registro(request):
    return render(request, 'blogdevnewsapp/registro.html')