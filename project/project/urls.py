from catalog import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'), 
]
