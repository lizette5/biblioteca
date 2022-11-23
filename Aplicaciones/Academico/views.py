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
    return redirect('inicio')

def deleteLibro(request, id):
    libro = Libro.objects.get(id = id)
    libro.delete()
    return redirect('inicio')

def editLibro(request, id):
    libro = Libro.objects.get(id=id)
    return render(request, 'libroEdit.html',{"libro": libro, "Genero":Genero.objects.all})

def modifyLibro(request, id):
    nombre= request.POST.get('nombre', False)
    autor = request.POST.get('autor', False)
    anio = request.POST.get('anio', False)
    genero= Genero.objects.get(id=request.POST.get('genero'))

    libro=Libro.objects.get(id=id)
    libro.nombre=nombre
    libro.autor = autor
    libro.anio = anio
    libro.genero = genero
    libro.save()

    return redirect('inicio')
