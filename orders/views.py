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
        return render(request, "orders/login.html", {"menssage": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/index.html")

# def login_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]

#     user = authenticate(request, username=username, password=password)

#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "orders/login.html", {"message":"invalid credentials"})


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out"})

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
        messages.add_message(request, messages.ERROR, 'Invalid Entry')
        return HttpResponseRedirect(reverse('register'))
    if not username:
        messages.add_message(request, messages.ERROR, 'Invalid Username')
        return HttpResponseRedirect(reverse('register'))
    if not password:
        messages.add_message(request, messages.ERROR, 'Invalid password')
        return HttpResponseRedirect(reverse('register'))

    check_user = User.objects.filter(username=username)
    if check_user:
        messages.add_message(request, messages.ERROR,
                             'Username already exists, try something else')
        return HttpResponseRedirect(reverse('register'))
    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.ERROR,
                             'email already exists, try something else')
        return HttpResponseRedirect(reverse('register'))
    if len(first_name) < 2:
        messages.add_message(request, messages.ERROR,
                             'First Name must be greater than 2 char')
        return HttpResponseRedirect(reverse('register'))
    if len(last_name) < 2:
        messages.add_message(request, messages.ERROR,
                             'Last Name must be greater than 2 char')
        return HttpResponseRedirect(reverse('register'))

    user = User.objects.create_user(
        username=username, first_name=first_name, last_name=last_name, email=email, password=password)
    user.save()
    login(request, user)

    # cart = Cart(user=request.user)
    # cart.save()
    messages.add_message(request, messages.SUCCESS,
                         'Registeration successful!')
    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    if request.method == 'GET':
        return render(request, 'orders/login.html')
    try:
        username = request.POST['username']
        password = request.POST['password']

    except KeyError:
        messages.add_message(request, messages.ERROR, 'Invalid Entry')
        return HttpResponseRedirect(reverse('login'))
    if not username:
        messages.add_message(request, messages.ERROR, 'Invalid Username')
        return HttpResponseRedirect(reverse('login'))
    if not password:
        messages.add_message(request, messages.ERROR, 'Invalid password')
        return HttpResponseRedirect(reverse('login'))

    user = authenticate(request, username=username, password=password)
    if not user:
        return render(request, 'orders/login.html', {'errmsg': 'Invalid credentials'})
    else:
        login(request, user)
        messages.add_message(request, messages.SUCCESS,
                             'Logged in successfully')
        return HttpResponseRedirect(reverse('index'))
