from django.db import models

# Create your models here.
class Genero(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre=models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self) :
        texto = "{0}"
        return texto.format(self.nombre)

class Libro(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre=models.CharField(max_length=50,blank=True, null=True)
    autor=models.CharField(max_length=30,blank=True, null=True)
    anio=models.PositiveSmallIntegerField(blank=True, null=True)
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE, blank=True, null=True)
    estado=models.BooleanField( blank=True, null=True, default=True)

    def __str__(self) :
        texto = "{0}"
        return texto.format(self.nombre)

class Usuario(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre=models.CharField(max_length=50, blank=True, null=True)
    apellidos=models.CharField(max_length=70, blank=True, null=True)
    dni=models.CharField(max_length=70, blank=True, null=True)

    def __str__(self) :
        texto = "{0}"
        return texto.format(self.nombre)


class Prestamo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    id_libro=models.ForeignKey(Libro, on_delete=models.CASCADE, blank=True, null=True)
    fecha=models.DateField(blank=True, null=True)

    def __str__(self) :
        texto = "{0} {1}"
        return texto.format(self.id_usuario.nombre,self.id_libro.nombre)

    
    

  