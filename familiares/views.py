from django.shortcuts import render
from familiares.models import familiares
# Create your views here.

def familiares_add(request):
    new_familiares = familiares.objects.all()
    context = {'new_familiares':new_familiares}
    return render(request,'index.html',context=context)
