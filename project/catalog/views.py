from django.shortcuts import render, redirect
from django.http import HttpResponse 
from.forms import UserForm 
from .models import Person

def about(request):
    return render(request,"firstapp/about.html")

def contact(request):
    return render(request,"firstapp/contact.html")

def index(request):     
    my_text = 'Изучаем модели Django'
    people_kol = Person.object_person.count()
    context = {'my_text': my_text, "people_kol": people_kol}
    return render(request, "firstapp/index.html", context)


"""
def my_form(request):     
    if request.method == "POST":
        userform = UserForm(request.POST)
    if userform.is_valid():
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = "<h2>Пользователь</h2><h3>Имя - {0}," \
     " Возраст – {1} </h3 >".format(name, age)
        return HttpResponse(output)
    userform = UserForm()
    return render(request, "firstapp/my_form.html", {"form": userform})

"""

def my_form(request):
    if request.method == "POST": 
        form = UserForm(request.POST) 
        if form.is_valid(): 
            form.save()

    my_text = 'Сведения о клиентах'
    people = Person.object_person.all()
    form = UserForm()
    context = {'my_text': my_text, "people": people, "form": form}
    return render(request, "firstapp/my_form.html", context)