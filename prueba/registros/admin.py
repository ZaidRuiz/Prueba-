from django.contrib import admin
from cursos.models import Cursos 
from .models import Alumnos, Comentario, Actividad, ComentarioContacto

# --- ALUMNOS ---
@admin.register(Alumnos)
class AdministrarModelo(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    list_filter = ('carrera', 'turno')

# --- COMENTARIOS ---
@admin.register(Comentario)
class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

# --- ACTIVIDAD ---
@admin.register(Actividad)
class AdministrarActividad(admin.ModelAdmin):
    list_display = ('id', 'curso', 'fecha_creacion')
    readonly_fields = ('fecha_creacion', 'id')

# --- COMENTARIO CONTACTO ---
@admin.register(ComentarioContacto)
class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')