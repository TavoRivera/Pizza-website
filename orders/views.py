from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def index(request):
    # verifica si el usuario está logueado
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"menssage_alert": "Invalid Username"})
    context = {
        "user": request.user
    }
    return render(request, "orders/index.html")


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

    # cart = Cart(user=request.user)
    # cart.save()
    return render(request, "orders/index.html", {"message_success": "Registration Successfull!"})


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
        return render(request, "orders/index.html", {"message_success": "Welcome!"})
