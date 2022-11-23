from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Aplicaciones.Academico.models import *
from django.template import RequestContext

# Create your views here.
def inicio(request):
    librosListados = Libro.objects.all()
    return render(request, "librosList.html", {"Libro" : librosListados})
	

def registerLibro(request):
    return render(request, 'librosAdd.html', {"Genero":Genero.objects.all})


def createLibro(request):
    libro = Libro.objects.create(
        nombre= request.POST.get('nombre', False),
        autor = request.POST.get('autor', False),
        anio = request.POST.get('anio', False),
        genero= Genero.objects.get(id=request.POST.get('genero')),
    )
    return render(request, 'librosList.html')

