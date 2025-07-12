from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL para la página de inicio
    # URL para la página de productos
    path('products/', views.products, name='products'),
    # URL para el ejemplo de mark_safe
    path('article/', views.article_detail, name='article_detail'),
    # URL de ejemplo para el detalle de un producto (usada en tarjeta_producto.html)
    path('products/<int:product_id>/',
         views.product_detail, name='product_detail'),
]
