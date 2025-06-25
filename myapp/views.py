from django.shortcuts import render
from .models import Producto, Categoria, Usuario, Pedido

# Create your views here.
def index(request):
    from datetime import datetime
    time_actual = datetime.now()
    contexto = {
        "mensaje": "Espero que aqui encuentres todo lo que necesitas. Aqui vas a encontrar todas las herramientas que necesites para que tu emprendimiento sea exitoso.",
        "time_actual": time_actual
    }
    return render(request, "myapp/index.html", context=contexto)
    

def lista_productos(request):
    productos = Producto.objects.all()
    contexto = {
        "productos": productos
    }
    return render(request, "myapp/lista_productos.html", context=contexto)

def lista_categorias(request):
    categorias = Categoria.objects.all()
    contexto = {
        "categorias": categorias
    }
    return render(request, "myapp/lista_categorias.html", context=contexto)

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    contexto = {
        "pedidos": pedidos
    }
    return render(request, "myapp/lista_pedidos.html", context=contexto)

