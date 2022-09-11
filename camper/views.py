from django.shortcuts import render, HttpResponse
from django.views import generic



def home(request):
    return render(request, "camper/home.html",{} )

def camper1(request):
    return render(request, "camper/camper1.html",{} )

def camper2(request):
    return render(request, "camper/camper2.html",{} )

def inquiry(request):
    return render(request, "camper/inquiry.html",{} )
