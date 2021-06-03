from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('cart', views.cart, name='cart'),
    path('orders', views.my_orders, name='orders'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
     path('delete_item', views.delete_item, name='delete_item'),
]
