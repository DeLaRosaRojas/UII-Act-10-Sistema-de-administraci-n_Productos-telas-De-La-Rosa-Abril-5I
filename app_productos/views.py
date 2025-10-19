from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 # Importa get_object_or_404 aquí
from django.urls import reverse

from .models import Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    return render(request, 'app_productos/index.html', {
        'productos': Producto.objects.all()
    })

def view_producto(request, id):
    # Aunque esta vista redirige, es buena práctica usar get_object_or_404
    producto = get_object_or_404(Producto, pk=id) 
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Extrae los datos limpiados del formulario (tu lógica original)
            # Aunque 'form.save()' es más conciso para ModelForms, mantengo tu estilo
            new_nombre = form.cleaned_data['nombre']
            new_categoria = form.cleaned_data['categoria']
            new_precio = form.cleaned_data['precio']
            new_stock = form.cleaned_data['stock']
            new_unidad_medida = form.cleaned_data['unidad_medida']

            # Crea y guarda el nuevo producto con los datos extraídos
            new_producto = Producto(
                nombre=new_nombre,
                categoria=new_categoria,
                precio=new_precio,
                stock=new_stock,
                unidad_medida=new_unidad_medida
            )
            new_producto.save()
            
            # ¡CAMBIO CLAVE! Redirige a la página 'index' después de un guardado exitoso
            return HttpResponseRedirect(reverse('index')) 
        else:
            # Si el formulario no es válido, vuelve a mostrar el formulario con los errores
            return render(request, 'app_productos/add.html', {
                'form': form # Pasa el formulario con los datos y errores para que se muestren
            })
    else:
        # Si es una solicitud GET, muestra un formulario vacío
        form = ProductoForm()
    
    return render(request, 'app_productos/add.html', {
        'form': form # Siempre pasa el formulario (vacío para GET, con errores para POST inválido)
    })

def edit(request, id):
    # ¡CAMBIO CLAVE! Usar get_object_or_404 para manejar casos donde el ID no existe
    producto = get_object_or_404(Producto, pk=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            # ¡CAMBIO CLAVE! Redirige a la página 'index' después de una edición exitosa
            return HttpResponseRedirect(reverse('index'))
        else:
            # Si el formulario no es válido, vuelve a mostrar el formulario con los errores
            return render(request, 'app_productos/edit.html', {
                'form': form, # Pasa el formulario con los datos y errores para que se muestren
                # 'success': False ya no es necesario si rediriges o muestras errores
            })
    else:
        # Para una solicitud GET, pre-rellena el formulario con los datos del producto existente
        form = ProductoForm(instance=producto)
    
    return render(request, 'app_productos/edit.html', {
        'form': form # Siempre pasa el formulario (pre-rellenado para GET, con errores para POST inválido)
    })

def delete(request, id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=id)
        producto.delete()
    return HttpResponseRedirect(reverse('index'))
    