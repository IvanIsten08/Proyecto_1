from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
]