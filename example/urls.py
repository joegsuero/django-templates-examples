from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para la página de inicio
    # URL para la página de productos
    path('productos/', views.productos, name='productos'),
    # URL para el ejemplo de mark_safe
    path('articulo/', views.articulo_detalle, name='articulo_detalle'),
    # URL de ejemplo para el detalle de un producto (usada en tarjeta_producto.html)
    path('productos/<int:producto_id>/',
         views.detalle_producto, name='detalle_producto'),
]
