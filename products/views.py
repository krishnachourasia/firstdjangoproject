from django.shortcuts import render, get_object_or_404
from products.models import Product
from .forms import ProductForm
# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_detial_view(request):

    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


def render_initial_data(request):
    initial_data = {
        "title": "this is my awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html',context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id= id)
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, 'products/product_detail.html', context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)

