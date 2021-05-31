from django.contrib import admin

from .models import Inventory, Topping, ItemCost, ToppingCount, Type, Size

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Topping)
admin.site.register(ItemCost)
admin.site.register(ToppingCount)
admin.site.register(Type)
admin.site.register(Size)
