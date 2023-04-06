
from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto

# Create your views here.


def producto_list(request):
    context = {'producto_list': Producto.objects.all()}
    return render(request, "app/producto_list.html", context)


def producto_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductoForm()
        else:
            producto = Producto.objects.get(pk=id)
            form = ProductoForm(instance=producto)
        return render(request, "app/producto_form.html", {'form': form})
    else:
        if id == 0:
            form = ProductoForm(request.POST)
        else:
            producto = Producto.objects.get(pk=id)
            form = ProductoForm(request.POST,instance= producto)
        if form.is_valid():
            form.save()
        return redirect('/productos/list')


def producto_delete(request,id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
    return redirect('/productos/list')
