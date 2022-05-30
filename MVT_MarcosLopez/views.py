from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    return HttpResponse('hola mundo')

def probando_template(request):
    context = {
        'nombre':'Marcos',
        'apellido':'Lopez',
        'fecha':datetime.now().date,
        'edades':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'index.html',context = context)