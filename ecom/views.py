from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import product, Category, cart, comments
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
    comment = comments()
    review = comments.objects.filter(item=product1)
    if request.method == 'POST':
        comment.item = product1
        comment.user = request.user
        comment.body = request.POST.get('body')
        duplicate = comments.objects.filter(user= request.user, item= product1)
        if duplicate:
            error = "you cannot post more than one"
            return render(request, 'ecom/detail.html', {'product':product1,'review':review, 'error': error})
        comment.save()
    

    return render(request, 'ecom/detail.html', {'product':product1,'review':review})

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

    