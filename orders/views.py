from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from decimal import Decimal
from .models import *

# Create your views here.


def index(request):
    # verifica si el usuario está logueado
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"menssage_alert": "Invalid Username"})
    # retornamos nuestro menú
    context = {
        'types': Type.objects.all(),
        'inventory': Inventory.objects.all(),
        'size':  Size.objects.all(),
        'toppings': Topping.objects.all(),
        'extra_allowed_count': 3

    }
    return render(request, "orders/index.html", context)

# def addItem_view(request):
#     try:
#         item_id = request.POST['item-id']
#     except:
#         item_id = None
#     try:
#         max_topping = request.POST['max_topping']
#     except:
#         None
#     try:
#         size = request.POST['size-select']
#     except:
#         size = None

#     toppings = []
#     if max_topping:
#         for i in max_topping:
#             try:
#                 top = request.POST[f'select-{i}']
#                 toppings.append(Topping.objects.get(pk=top))
#             except:
#                 pass
#     item = Inventory.objects.get(pk=item_id)

#     cart = Orderr.objects.get(user=request.user)
#     cart_item = Orderr(order_id=cart, item=item)


def add_to_cart(request):
    if request.method == 'POST':
        size = request.POST["item"]
        topp = request.POST.getlist("toppings-selected")
        cantidad = request.POST["qty"]

        cart_item = ItemCost.objects.get(pk=size)
        item = cart_item.itemcost.get()
        price = cart_item.amount

        number_of_toppings = int(len(topp))
        to_cart = Orderr.objects.create(
            qty=cantidad, status='Initiated', amount=price, user_id=request.user.id)

        # verifica si el item es personalizable
        if item.customizable is True:
            for n in topp:
                topping = Topping.objects.get(pk=n)
                to_cart.item_topping.add(topping)

            # loop over toppings
            for c in ToppingCount.objects.all():
                for p in c.inventory.all():
                    if p.id == cart_item.id:
                        # check for amount of selected topping
                        if number_of_toppings == int(c.count):
                            # if subs then topping should add amount to price
                            if str(item.item_type) == "subs":
                                price = price + c.amount
                            else:
                                # if not subs price should be topping price

                                price = c.amount

        price = float(price) * int(cantidad)

        to_cart.item.add(cart_item)
        to_cart.amount = price

        to_cart.save()
        messages.success(request, f'Item: {to_cart} added to cart!')
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "orders/index.html")


def cart(request):
    orders =  Orderr.objects.filter(user_id=request.user.id)
    total = Decimal(0)
    cart_item_count = 0
        
    total_id = []
    for order in orders:
        if order.status == 'Initiated':
            total_id.append(order.id)
            cart_item_count = len(total_id)
            total += Decimal(order.amount)
    context = {
        "inventory": Inventory.objects.all(),
        "itemcost": ItemCost.objects.all(),
        "orders": orders,
        "total": total,
        "total_id": total_id,
        "cart_item_count": cart_item_count
    }
    return render(request, 'orders/cart.html', context)

def delete_item(request):
    item_id = request.POST["item_id"]  
    Orderr.objects.get(pk=item_id).delete()
        
        
        
    # after delete redirect to previous page
    return HttpResponseRedirect('cart')


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message_success": "You Logged out"})

# crea un nuevo usuario


def register(request):
    if request.method == 'GET':
        return render(request, 'orders/register.html')
    try:
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email = request.POST["email"]

    except KeyError:
        return render(request, "orders/register.html", {"message_alert": "Invalid Entry"})
    if not username:
        return render(request, "orders/register.html", {"message_alert": "Invalid Username"})
    if not password:
        return render(request, "orders/register.html", {"message_alert": "Invalid Password"})

    check_user = User.objects.filter(username=username)
    if check_user:
        return render(request, "orders/register.html", {"message_alert": "Username already exists, try something else"})
    if User.objects.filter(email=email).exists():
        return render(request, "orders/register.html", {"message_alert": "email already exists, try something else"})
    if len(first_name) < 2:
        return render(request, "orders/register.html", {"message_alert": "First Name must be greater than 2 char"})
    if len(last_name) < 2:
        return render(request, "orders/register.html", {"message_alert": "Last Name must be greater than 2 char"})

    user = User.objects.create_user(
        username=username, first_name=first_name, last_name=last_name, email=email, password=password)
    user.save()
    login(request, user)

 
    messages.success(request, f" Now you're registered!")
    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    if request.method == 'GET':
        return render(request, 'orders/login.html')
    try:
        username = request.POST['username']
        password = request.POST['password']

    except KeyError:
        return render(request, "orders/login.html", {"message_alert": "Invalid Entry"})
    if not username:
        return render(request, "orders/login.html", {"message_alert": "Invalid Username"})
    if not password:
        return render(request, "orders/login.html", {"message_alert": "Invalid Password"})

    user = authenticate(request, username=username, password=password)
    if not user:
        return render(request, 'orders/login.html', {'message_alert': 'Invalid credentials'})
    else:
        login(request, user)
        # render(request, "orders/index.html", {"message_success": "Welcome!"})
        return HttpResponseRedirect(reverse('index'))


def my_orders(request):
    return render(request, 'orders/orders.html')
