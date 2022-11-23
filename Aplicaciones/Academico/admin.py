from django.contrib import admin
from .models import Genero
from .models import Libro
from .models import Usuario
from .models import Prestamo
# Register your models here.
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Prestamo)