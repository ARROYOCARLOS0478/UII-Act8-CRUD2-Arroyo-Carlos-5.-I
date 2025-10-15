from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos # Importa el modelo Productos que creamos

# Vista para listar todos los productos
def listar_productos(request):
    productos = Productos.objects.all().order_by('nombre') # Ordenamos por nombre
    return render(request, 'listar_productos.html', {'productos': productos})

# Vista para ver los detalles de un producto específico
def ver_producto(request, id_producto):
    # Usamos 'id' para la clave primaria del modelo Productos
    producto = get_object_or_404(Productos, id=id_producto)
    return render(request, 'ver_producto.html', {'producto': producto})

# Vista para agregar un nuevo producto
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST.get('descripcion', '') # Es opcional en el modelo
        precio = request.POST['precio']
        stock = request.POST.get('stock', 0) # Es opcional y tiene un default en el modelo
        modelo = request.POST.get('modelo', '') # Es opcional en el modelo

        # Convertimos precio y stock a sus tipos correctos
        try:
            precio = float(precio) # O Decimal(precio) si quieres más precisión
            stock = int(stock)
        except ValueError:
            # Aquí podrías manejar un error, por ahora redirigimos con un mensaje
            # O podrías re-renderizar el formulario con errores
            return redirect('agregar_producto') # Ejemplo básico de manejo de error

        Productos.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            modelo=modelo
        )
        return redirect('listar_productos') # Redirige a la vista de lista de productos
    return render(request, 'agregar_producto.html')

# Vista para editar un producto existente
def editar_producto(request, id_producto):
    producto = get_object_or_404(Productos, id=id_producto)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST.get('descripcion', '')
        producto.precio = request.POST['precio']
        producto.stock = request.POST.get('stock', 0)
        producto.modelo = request.POST.get('modelo', '')

        # Convertimos precio y stock a sus tipos correctos
        try:
            producto.precio = float(producto.precio) # O Decimal(producto.precio)
            producto.stock = int(producto.stock)
        except ValueError:
            return redirect('editar_producto', id_producto=id_producto) # Manejo básico de error

        producto.save()
        return redirect('listar_productos') # O podrías redirigir a 'ver_producto'
    return render(request, 'editar_producto.html', {'producto': producto})

# Vista para borrar un producto existente
def borrar_producto(request, id_producto):
    producto = get_object_or_404(Productos, id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'borrar_producto.html', {'producto': producto})