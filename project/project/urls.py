from catalog import views 
from django.contrib import admin
from django.urls import path, include
from django import forms
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('my_form/', views.my_form, name='my_form'), 
    path('my_form/edit_form/<int:id>/', views.edit_form, name='edit_form'),
    path('my_form/delete/<int:id>/', views.delete),
    #path('form_up_pdf/', views.form_up_pdf, name='form_up_pdf'),
    path('form_up_img/', views.form_up_img, name='form_up_img'),
    path('form_up_img/delete_img/<int:id>/', views.delete_img),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)