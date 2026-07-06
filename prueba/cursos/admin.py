from django.contrib import admin
from .models import Cursos

@admin.register(Cursos)
class AdministrarCursos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre_curso', 'duracion_horas', 'activo', 'created')
    search_fields = ('nombre_curso', 'descripcion')
    date_hierarchy = 'created'
    list_filter = ('activo', 'duracion_horas')
    fields = ('nombre_curso', 'descripcion', 'duracion_horas', 'imagen', 'activo', 'created', 'updated')