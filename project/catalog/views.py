from django.shortcuts import render
from django.http import HttpResponse 
from.forms import UserForm 

def about(request):
    return render(request,"firstapp/about.html")

def contact(request):
    return render(request,"firstapp/contact.html")

def index(request):     
    my_text = 'Изучаем формы Django'
    context = {'my_text': my_text} 
    return render(request, "firstapp/index.html", context) 


def my_form(request):     
    my_form = UserForm()     
    context = {"form": my_form} 
    return render(request, "firstapp/my_form.html", context) 
