from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto

# Create your views here.

def producto_list(request):
    context = {'producto_list': Producto.objects.all()}
    return render(request, "app/producto_list.html", context)

def producto_form(request, id = 0): # id por defecto es 0
    if request.method == "GET": # Metodo GET. "http://127.0.0.1:8000/productos" o "http://127.0.0.1:8000/productos/1".
        if id == 0: # Vista por defecto, formulario vacio
            form = ProductoForm()
        else: # Vista con datos, formulario con datos del producto elegido
            producto = Producto.objects.get(pk = id)
            form = ProductoForm(instance = producto)

        return render(request, "app/producto_form.html", {'form': form})

    else: # Metodo POST
        if id == 0: # Guardar producto
            form = ProductoForm(request.POST)
        else: # Editar producto
            producto = Producto.objects.get(pk = id)
            form = ProductoForm(request.POST, instance = producto)

        # Guardar o editar
        if form.is_valid():
            form.save()

        return redirect('/productos/list')

def producto_delete(request, id):
    producto = Producto.objects.get(pk = id)
    producto.delete()
    return redirect('/productos/list')
