from django.apps import AppConfig


class InicioConfig(AppConfig):
    name = 'inicio'
<<<<<<< HEAD
def principal(request):
    print("ENTRE A PRINCIPAL")
    contexto = {
        "user_text": "Principal",
        "user_subtext": "DGS",
        "user_img": "inicio/images/home.png"
    }
    return render(request, "inicio/principal.html", contexto)
=======
>>>>>>> b8b5b7d0ca931f96deaea1be431ecce7153bdb35
