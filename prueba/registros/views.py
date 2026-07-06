from django.shortcuts import render
<<<<<<< HEAD
from .models import Alumnos, ComentarioContacto #Accedemos al modelo Alumnos que contiene la estructura de la tabla.
from .models import Comentario
from .forms import ComentarioContactoForm

# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all() # all recuperar todos los objetos del modelo (registros de la tabla alumnos)
    comentario = Comentario.objects.all()
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})
    #indicamso el lugar donde se renderiza el resultado de esta vista y enviamos la lista de alumnos recuperados
=======
from .models import Alumnos
from .forms import ComentarioContactoForm

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def contacto(request):
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {'form': form})
>>>>>>> b8b5b7d0ca931f96deaea1be431ecce7153bdb35

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
<<<<<<< HEAD
            comentarios = ComentarioContacto.objects.all()
            return render(request, 'registros/consultar_comentarios.html', {'comentarios': comentarios})
    form = ComentarioContactoForm()
    #Si sale mal reenvian al formulario los datos ingresados
    return render(request, 'registros/contacto.html', {'form': form})

def contacto(request):
    return render(request, "registros/contacto.html")

def consultar_comentarios(request):
    comentarios = ComentarioContacto.objects.all()

    return render(
        request,
        "registros/consultar_comentarios.html",
        {"comentarios": comentarios}
    )
=======
            return render(request, 'registros/contacto.html', {'form': ComentarioContactoForm(), 'mensaje': 'Enviado'})
    return render(request, 'registros/contacto.html', {'form': ComentarioContactoForm()})
>>>>>>> b8b5b7d0ca931f96deaea1be431ecce7153bdb35
