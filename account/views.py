from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm
from product.models import Product
from django.http import Http404


def index(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        products = Product.objects.filter(hunter=user_id)
        return render(request, 'account/index.html', {'products': products})
    else:
        return redirect('account:signup')


# @login_required
'''   
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                messages.error(request,"Username is already taken !")
                return render(request, 'account/signup.html')

            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('account:index')
        else:
            messages.error(request,"Password doesn\'t matched")
            return render(request, 'account/signup.html')

    else:
        return render(request, 'account/signup.html')


def signin(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('account:index')
        else:
            messages.error(request,"username or password is incorrect")
            return render(request, 'account/signin.html')
    else:
        return render(request, 'account/signin.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('product:index')
'''


@login_required
def delete(request, p_id):
    if request.user.is_authenticated:
        try:
            product = get_object_or_404(Product, pk=p_id)  # , hunter=user_id)
            product.delete()
            return redirect('account:index')
        except Http404:
            return redirect('account:index')

    return redirect('account:index')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            auth.login(request, user)
            messages.success(
                request, f'Accout created succefully for {username}')
            return redirect('account:index')
    else:
        # if a GET (or any other method) we'll create a blank form
        form = SignupForm()
    # we'll create either a blank form or a populated form
    return render(request, 'account/signup.html', {'form': form})
