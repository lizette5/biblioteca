from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('inicio', views.inicio, name ='inicio'),
    path('libro/registerLibro', views.registerLibro, name ='registerLibro'),
    path('libro/delete/<id>', views.deleteLibro, name ='deleteLibro'),
    path('libro/createLibro', views.createLibro, name ='createLibro'),
    path('libro/edit/<id>', views.editLibro, name = "editLibro"),
    path('libro/modify/<id>', views.modifyLibro, name = "modifyLibro"),
    


    path('persona/list', views.listUsuario, name ='listPersona'),
    path('persona/register', views.registerUsuario, name ='registerPersona'),
    path('persona/delete/<id>', views.deleteUsuario, name ='deletePersona'),
    path('persona/createPersona', views.createUsuario, name ='createPersona'),
    path('persona/edit/<id>', views.editUsuario, name = "editPersona"),
    path('persona/modify/<id>', views.modifyUsuario, name = "modifyPersona"),


    path('prestamo', views.prestar, name = "prestarLibro"),
    path('prestamoList', views.prestarList, name = "prestarLibroList"),
    path('prestarYa', views.realizarPrestamo, name = "realizarPrestamo"),
    
]