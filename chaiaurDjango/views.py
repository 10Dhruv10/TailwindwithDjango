from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def indextwo(request):
    return render(request, 'website/index2.html')

def About(request):
    return HttpResponse("About Page")

def contactus(request):
    return HttpResponse("This is Contact Page")