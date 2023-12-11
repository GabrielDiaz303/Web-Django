from django.shortcuts import render
from .models import Mascota

# Create your views here.
def perygat(request):
    mascotas = Mascota.objects.all()
    return render(request, "perrosygatos/perrosygatos.html",{"mascotas":mascotas} )