from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('article/', views.article_detail, name='article_detail'),
    path('products/<int:product_id>/',
         views.product_detail, name='product_detail'),
]
