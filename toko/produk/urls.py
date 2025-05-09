from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_produk, name='list_produk'),
    path('tambah/', views.tambah_produk, name='tambah_produk'),
    path('edit/<int:pk>/', views.update_produk, name='update_produk'),
    path('hapus/<int:pk>/', views.hapus_produk, name='hapus_produk'),
]