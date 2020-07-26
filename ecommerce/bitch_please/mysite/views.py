from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from .models import Order, Product, Cart


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        home_basics = Product.objects.all().filter(tags__name='Home Basics')
        sports_and_fitness = Product.objects.all().filter(tags__name='Sports and fitness')
        appliances_electronics = Product.objects.all().filter(tags__name='Appliances, Electronics')
        fasion = Product.objects.all().filter(tags__name='Fasion')
        audiable_and_educational = Product.objects.all().filter(tags__name='Audible & Educational')
        beauty_health_grocery = Product.objects.all().filter(tags__name='Beauty, Health, Grocery')

        context = {
            'Home_Basics': home_basics,
            'Sports_and_fitness': sports_and_fitness,
            'Appliances_Electronics': appliances_electronics,
            'Fasion': fasion,
            'Audible_Educational': audiable_and_educational,
            'Beauty_Health_Grocery': beauty_health_grocery
        }
        return render(request, 'home.html', context)
    else:
        return redirect('login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context = {'error': "Invalid login credentials."}
            return redirect('login')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username)
            print(raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {
        'form': form
    })


def mycart_view(request):
    user_cart = Cart.objects.filter(customer=request.user)
    return render(request, 'mycart.html', {'user_cart': user_cart})


def myorders_view(request):
    user_orders = Order.objects.filter(customer=request.user)
    print(user_orders)
    return render(request, 'myorders.html', {'user_orders': user_orders})


def product_view(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        quantity = request.POST['quantity']
        address = request.POST['address']
        mode_of_payment = request.POST['mode_of_payment']

        new_order = Order.objects.create(customer=request.user, product=product, quantity=quantity,
                                         mode_of_payment=mode_of_payment,
                                         status='Pending', address=address)
        new_order.save()
    return render(request, 'product.html', {"product": product})


def logout_view(request):
    logout(request)
    return redirect('login')


def add_to_cart_view(request, pk):
    product = Product.objects.get(id=pk)
    user = request.user

    cart_obj = Cart.objects.create(product=product, customer=user)
    cart_obj.save()

    return redirect('home')


def search_view(request):
    product = request.GET.get('product')
    products = Product.objects.filter(name__contains=product)

    return render(request, 'search.html',{'products': products})
