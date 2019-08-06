from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Voter
from .forms import ProductForm


def index(request):
    products = Product.objects.order_by('-votes')

    return render(request, 'product/index.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.product_url = request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.hunter = request.user
            product.save()

            return redirect('/product/detail/'+str(product.id))
        else:
            messages.error(request, 'Please input all fields')
            return render(request, 'product/add.html')
    else:
        return render(request, 'product/add.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/detail.html', {'product': product})


@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        if Voter.objects.filter(user=request.user.id, product=product_id).exists():
            return redirect('/product/detail/'+str(product_id))
        else:
            product = get_object_or_404(Product, pk=product_id)
            product.votes += 1
            product.save()
            voter_count = Voter(product=product, user=request.user)
            voter_count.save()
            return redirect('/product/detail/'+str(product.id))

    return redirect('/product/detail/'+str(product_id))


@login_required
def edit(request, p_id):
    product = get_object_or_404(Product, pk=p_id) 
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, isinstance=product)
        if form.is_valid :
            ProductTitle = form.cleaned_data['title']
            form.save
            messages.success(request,ProductTitle+" Successfully edited ")
            return redirect('account:index')
    else:
         # user wants to edit a product
        form = ProductForm(instance=Product)
        return render(request, 'product/edit.html',{"form":form,"IdProduct":p_id})
'''def edit(request,p_id):
    product = get_object_or_404(Product, pk=p_id)
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url']:
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.product_url = request.POST['url']
            if 'icon' in request.FILES :
                product.icon = request.FILES['icon']
            if 'image' in request.FILES :    
                product.image = request.FILES['image']
            product.hunter = request.user
            product.save()

            messages.success(request,product.title+" Successfully edited ")
            return redirect('/accounts/')
        else:
            messages.error(request,'Please input all fields')
            return render(request, 'product/edit.html')
    else:
        # user wants to edit a product
        return render(request, 'product/edit.html',{"product":product})
'''
