from django.db import models

class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    descripcion = models.TextField(verbose_name="Descripción del Curso")
    duracion_horas = models.IntegerField(verbose_name="Duración en Horas")
    imagen = models.ImageField(null=True, upload_to="cursos_fotos", verbose_name="Imagen del Curso")
    activo = models.BooleanField(default=True, verbose_name="¿Está Activo?") 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['created']

    def __str__(self):
        return self.nombre_curso