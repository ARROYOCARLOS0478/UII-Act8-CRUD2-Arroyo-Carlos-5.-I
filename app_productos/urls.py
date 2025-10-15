from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('ver/<int:id_producto>/', views.ver_producto, name='ver_producto'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    path('borrar/<int:id_producto>/', views.borrar_producto, name='borrar_producto'),
]