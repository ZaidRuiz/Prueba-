from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def contacto(request):
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {'form': form})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registros/contacto.html', {'form': ComentarioContactoForm(), 'mensaje': 'Enviado'})
    return render(request, 'registros/contacto.html', {'form': ComentarioContactoForm()})