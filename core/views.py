from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "core/index.html" )
def about(request):
    return render(request, "core/nosotros.html" )

def contact(request):
    return render(request, "core/contacto.html" )
def tienda(request):
    return render(request, "core/tienda.html" )