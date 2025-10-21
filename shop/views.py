from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# List of all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Single product detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

# Add new product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'action': 'Create'})

# Update existing product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'action': 'Update'})

# Delete product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})