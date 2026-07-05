from django.db import models
from ckeditor.fields import RichTextField
# IMPORTANTE: Esta línea conecta la app 'cursos' con 'registros'
from cursos.models import Cursos 

class Alumnos(models.Model):
    matricula = models.CharField(max_length=12, verbose_name="Matricula")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    carrera = models.CharField(max_length=100, verbose_name="Carrera")
    turno = models.CharField(max_length=20, verbose_name="Turno")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Foto")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario") 

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-created'] 

class Actividad(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave de la actividad")
    # Ahora 'curso' usa el modelo importado correctamente
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Nombre del curso")
    descripcion = RichTextField(verbose_name="Descripción de la actividad")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"

    def __str__(self):
        return f"{self.curso.nombre_curso} - Actividad {self.id}"

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario") 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado") 

    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje