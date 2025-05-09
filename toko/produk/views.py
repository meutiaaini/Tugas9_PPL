from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produk
from .forms import ProdukForm

def list_produk(request):
    produk = Produk.objects.all()
    return render(request, 'produk/list.html', {'produk': produk})

def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil ditambahkan.')
            return redirect('list_produk')
    else:
        form = ProdukForm()
    return render(request, 'produk/form.html', {'form': form, 'aksi': 'Tambah'})

def update_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil diperbarui.')
            return redirect('list_produk')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk/form.html', {'form': form, 'aksi': 'Edit'})

def hapus_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    produk.delete()
    messages.success(request, 'Produk berhasil dihapus.')
    return redirect('list_produk')