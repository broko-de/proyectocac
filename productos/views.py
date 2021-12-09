from django.shortcuts import redirect, render
from django.http import HttpResponse
from productos.forms import ProductoForm

from productos.models import Producto

# Create your views here.


def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def productos(request):
    productos = Producto.objects.all
    return render(request,'productos/index.html',{'productos':productos})

def crear(request):
    formulario = ProductoForm(request.POST or None,request.FILES or None)
    #CUANDO EL FORMULARIO SE ENVIA CON DATOS
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request,'productos/crear.html',{'formulario':formulario})

def editar(request,id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(request.POST or None,request.FILES or None,instance=producto)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request,'productos/editar.html',{'formulario':formulario})

def eliminar(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')
