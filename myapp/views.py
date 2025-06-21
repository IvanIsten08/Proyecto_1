from django.shortcuts import render

# Create your views here.
def index(request):
    contexto = {
        "mensaje": "Espero que aqui encuentres todo lo que necesitas."
    }
    return render(request, "myapp/index.html", contexto)
    