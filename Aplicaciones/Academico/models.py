from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre=models.CharField(max_length=50)
    
    def __str__(self) :
        texto = "{0}"
        return texto.format(self.nombre)

class Libro(models.Model):
    nombre=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    anio=models.PositiveSmallIntegerField()
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE)
    estado=models.BooleanField()

    def __str__(self) :
        texto = "{0}"
        return texto.format(self.nombre)

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=70)
    dni=models.CharField(max_length=70)

    def __str__(self) :
        texto = "{0} {1}"
        return texto.format(self.nombre,self.apellidos)


class Prestamo(models.Model):
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha=models.DateField()

    def __str__(self) :
        texto = "{0} ({1})"
        return texto.format(self.id_usuario,self.id_libro)

    
    

  