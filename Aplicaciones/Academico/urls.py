from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('libro/registerLibro', views.registerLibro, name ='registerLibro'),
    path('libro/createLibro', views.createLibro, name ='createLibro'),
    
]