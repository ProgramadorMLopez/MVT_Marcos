from django.shortcuts import render
from familiares.models import familiares
# Create your views here.

def familiares_add(request):
    familia_nuevo =  familiares.objects.create(
        nombre = 'Laura',
        apellido = 'Ibarra',
        edad = 22,
        fecha_nacimiento = '2000-01-22'
    )
    context = {'familia_nuevo':familia_nuevo}
    return render(request,'index.html',context=context)
