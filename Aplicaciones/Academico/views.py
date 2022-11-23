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



def listUsuario(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarioList.html", {"usuario" : usuarios})
	


def registerUsuario(request):
    return render(request, 'usuarioAdd.html', {"usuario":Usuario.objects.all})


def createUsuario(request):
    usuario = Usuario.objects.create(
        nombre= request.POST.get('nombre', False),
        apellidos = request.POST.get('apellidos', False),
        dni = request.POST.get('dni', False),
        
    )
    return redirect('inicio')

def deleteUsuario(request, id):
    usuario = Libro.objects.get(id = id)
    usuario.delete()
    return redirect('inicio')

def editUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'usuarioEdit.html',{"usuario": usuario})

def modifyUsuario(request, id):
    nombre= request.POST.get('nombre', False)
    apellidos = request.POST.get('apellidos', False)
    dni = request.POST.get('dni', False)
    usuario=Usuario.objects.get(id=id)
    usuario.nombre=nombre
    usuario.autor = apellidos
    usuario.anio = dni
    usuario.save()

    return redirect('inicio')


def prestar(request):
    libros = Libro.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'prestar.html',{ "Persona": usuarios,"Libro": libros})

def realizarPrestamo(request):
    prestamo = Prestamo.objects.create(
        id_usuario= Usuario.objects.get(id=request.POST.get('id_usuario')),
        id_libro = Libro.objects.get(id=request.POST.get('id_libro')),
        fecha = request.POST.get('fecha', False),
        
    )
    return redirect('inicio')


def prestarList(request):
    libros = Libro.objects.all()
    usuarios = Usuario.objects.all()
    prestamo = Prestamo.objects.all()
    return render(request, 'prestarList.html',{ "prestamo": prestamo})