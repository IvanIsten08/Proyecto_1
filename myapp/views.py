from django.shortcuts import render

# Create your views here.
def index(request):
    from datetime import datetime
    time_actual = datetime.now()
    contexto = {
        "mensaje": "Espero que aqui encuentres todo lo que necesitas. Aqui vas a encontrar todas las herramientas que necesites para que tu emprendimiento sea exitoso.",
        "time_actual": time_actual
    }
    return render(request, "myapp/index.html", context=contexto)
    