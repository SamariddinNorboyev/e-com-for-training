from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.core.paginator import Paginator
from .forms import CreateForm, EditForm
# Create your views here.
def home(request):
    products = Product.objects.all()
    q = request.GET.get('q')
    if q and q!='None':
        products = Product.objects.filter(name__icontains = q)
    paginator = Paginator(products, 2)
    pnumber = request.GET.get('page')
    products = paginator.get_page(pnumber)
    return render(request, 'products/list.html', {'products': products,'q': q})

def create(request):
    if request.method == 'POST': 
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:home_page')
        return render(request, 'products/create.html', context={'form': form})
    form = CreateForm()
    return render(request, 'products/create.html', context={'form': form})

def delete(request, id):
    p = Product.objects.filter(id = id)
    p.delete()
    return redirect('products:home_page')
def view(request, id):
    p = Product.objects.filter(id = id).first()
    return render(request, 'products/view.html', context={'product': p})
    
def edit(request, id):
    if request.method == 'POST': 
        product = Product.objects.filter(id = id).first()
        form = EditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:home_page')
        return render(request, 'products/edit.html', context={'form': form})
    product = Product.objects.filter(id = id).first()
    form = EditForm(instance=product)
    return render(request, 'products/edit.html', context={'form': form, 'product': product})