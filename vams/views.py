from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):    
    return render(request, 'index.html')

def servicios(request):    
    return render(request, 'servicios.html')

def nosotros(request):    
    return render(request, 'sobrenosotros.html')

def catalogo01(request):
    return render(request, 'aretes.html')

def catalogo02(request):
    return render(request, 'collares.html')



