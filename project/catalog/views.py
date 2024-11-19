from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return render(request,"firstapp/index.html")

def about(request):
    return render(request,"firstapp/about.html")

def contact(request):
    return render(request,"firstapp/contact.html")