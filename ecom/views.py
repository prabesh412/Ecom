from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import product, Category, cart
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.
def frontpage(request):
    products = product.objects.all
    category = Category.objects.all()
    name = [] 

    for categorys in category:
        name.append(categorys.name)
    
    return render(request, 'ecom/frontpage.html', { 'name': name, 'product': products})


def detail(request, product_id1):
    product1 = get_object_or_404(product, pk=product_id1)

    return render(request, 'ecom/detail.html', {'product':product1})

@login_required
def cart1(request,product_id):
    cart2= cart()
    cart1 = cart.objects.filter(customer=request.user)
    if product_id != 0:
        product1 = get_object_or_404(product, pk=product_id)
        for carts in cart1:
            if carts.products == product1:
                return render(request, 'ecom/detail.html', {'product':product1})
        cart2.products = product1
        cart2.customer = request.user
        cart2.save()
        return render(request, 'ecom/detail.html', {'product':product1})

    return render(request,'ecom/cart.html', {'cart': cart1})



def items(request, item):

    products= product.objects.all()
    return render(request,'ecom/items.html', {'item':item, 'product': products})


def search1(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        products = product.objects.filter(product_name__icontains=searched)
        return render(request, "ecom/search.html", {'data': searched, 'product':products})

    