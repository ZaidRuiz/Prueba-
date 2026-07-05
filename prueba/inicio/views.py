from django.shortcuts import render,HttpResponse


# Create your views here.

#menu="""
#    <a href="/">Home</a>
#    <a href="/formulario">Registrar</a>
#    <a href="/contacto">Contactanos</a>
#    <a href="/nombre">About me</a>
#"""


def principal (request):
#    contenido="<h1>Hola Django</h1>"
#    return HttpResponse(menu+contenido)
     return render (request,"inicio/principal.html")

def minombre (request):
    #contenido="<h1>Zaid Martinez Ruiz</h1>"
    #return HttpResponse(menu+contenido)
    return render (request, "inicio/nombre.html")


def contacto(request):
    #contenido="""<h2>Contacto</h2>
    #    <p>Nombre: <input type="text" name="nombre"></p>
    #    <p>Mensaje:</p><p><textarea cols="50" rows="10"></textarea></р>
    #    ‹p><input type="Button" name="enviar" value="Enviar"/></p›"""
    #return HttpResponse(menu+contenido)
    return render (request, "inicio/contacto.html")


def formulario(request):
#contenido="""<h2> Registrar </h2>
 #  Matricula: <input type="text" name="matricula"</p>
  # <p>Nombre: <input type="text" name="nombre"</p>
   #<p>Carrera:
    #   <select name="carerra">
     #      ‹option>ING. DGS</option>
      #     <option>ING. EVND</option>
       #</select>
   #</p>
   #<input type="radio" name="turno" value="matutino">Matutino
   #<input type="radio" name="turno" value="vespertino">Vespertino
   #<p><input type="Button" name="enviar" value="Enviar"</p>"""
    #return HttpResponse(menu+contenido)
    return render (request, "inicio/formulario.html")



def ejemplo(request):
    return render (request, "inicio/ejemplo.html")