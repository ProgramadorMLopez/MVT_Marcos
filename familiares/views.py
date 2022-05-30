from django.shortcuts import render
from familiares.models import familiares
# Create your views here.

def familiares_add(request):
    familiares_nuevo =  familiares.objects.create(
        nombre = 'Laura',
        apellido = 'Ibarra',
        edad = 22,
        fecha_nacimiento = '2000-01-22',
        dni = '12345',
    )
    context = {'familiares_nuevo':familiares_nuevo}
    return render(request,'index.html',context=context)
