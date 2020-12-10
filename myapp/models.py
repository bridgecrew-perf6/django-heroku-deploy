from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)


class Editorial(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '%s' % (self.nombre)

# el codigo isnb, fecha de publicación, cantidad páginas, numero de edición,
# idioma, son información propias de la editorial_libro 
class LibroEditorial(models.Model):
    isbn = models.BigIntegerField(unique=True)
    # el título puede repetirse, lo que no puede repetirse es el isbn
    titulo = models.CharField(max_length=80)
    fecha_publicacion = models.DateField(auto_now=False)
    cantidad_paginas = models.PositiveSmallIntegerField(null=False)
    edicion = models.PositiveSmallIntegerField(null=False, default=1)
    idioma = models.CharField(max_length=30)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return '%s, %s Edición' % (self.titulo, self.edicion)