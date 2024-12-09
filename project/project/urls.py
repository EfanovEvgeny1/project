from catalog import views 
from django.contrib import admin
from django.urls import path
from django import forms


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('my_form/', views.my_form, name='my_form'), 
]
