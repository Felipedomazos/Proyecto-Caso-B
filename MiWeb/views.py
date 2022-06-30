from itertools import product
from sqlite3 import DateFromTicks
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from .forms import ProductoForm

# Create your views here.

def Interfaz(request):
    return render(request, 'MiWeb/Interfaz.html')


def Fundacion(request):
    return render(request, 'MiWeb/Fundacion.html')


def Nosotros(request):
    return render(request, 'MiWeb/Nosotros.html')


def Hortalizas(request):
    return render(request, 'MiWeb/Hortalizas.html')

def Aromaticas(request):
    return render(request, 'MiWeb/Aromaticas.html')


def MacetasGrandes(request):
    return render(request, 'MiWeb/MacetasGrandes.html')


def MacetasPequenas(request):
    return render(request, 'MiWeb/MacetasPequenas.html')


def FertilizantesInorganicos(request):
    return render(request, 'MiWeb/FertilizantesInorganicos.html')


def FertilizantesOrganicos(request):
    return render(request, 'MiWeb/FertilizantesOrganicos.html')


def Productos(request):
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'MiWeb/Productos.html', datos)


def agregar_producto(request):
    datos = {
        'form': ProductoForm()
    }

    if request.method== 'POST' :
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Agregado Correctamente"
        else:
            datos["form"] = formulario
            
    return render(request, 'MiWeb/producto/agregar.html', datos)


def listar_productos(request):
    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }

    return render(request, 'MiWeb/producto/listar.html', datos)


def modificar_producto(request, idProducto):

    producto = get_object_or_404(Producto, idProducto=idProducto)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method== 'POST' :
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario

    return render(request, 'MiWeb/producto/modificar.html', data)


def eliminar_producto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    producto.delete()
    return redirect(to="listar_productos")
