from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse('hola mundo')

def probando_template(request):
    return render(request,'index.html',context = {})