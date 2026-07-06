from django.contrib import admin
<<<<<<< HEAD
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #Campos que se muestran pero no se pueden modificar
    list_display = ('matricula', 'nombre', 'carrera', 'turno') #Una tupla o lista con los nombres de los campos que quieres que aparezcan como columnas.
    search_fields = ('matricula', 'nombre', 'carrera', 'turno') #Habilita una barra de búsqueda.
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno') #Activa un panel lateral derecho para filtrar los registros por campos específicos (fechas, booleanos, llaves foráneas).
    list_editable = ('nombre', 'turno')
admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentario(admin.ModelAdmin):
    list_display = ('id', 'coment',)
    search_fields = ('id', 'created',)
    date_hierarchy = 'created'
    list_filter = ('created', 'id')
    #exclude = ('coment',) #excluimos el campo que aparecera en el formulario de la tabla
admin.site.register(Comentario, AdministrarComentario)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
=======
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
>>>>>>> b8b5b7d0ca931f96deaea1be431ecce7153bdb35
