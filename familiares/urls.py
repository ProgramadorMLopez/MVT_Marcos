from django.contrib import admin
from django.urls import path
from familiares.views import familiares_add

urlpatterns = [
    path('',familiares_add,name='familiares'),
]
