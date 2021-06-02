from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# tamaño de los items (small, large etc)


class Size(models.Model):
    size = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.size}"

# tipo de items (pizza, subs, salads etc)


class Type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"

# lista de aderezos


class Topping(models.Model):
    item = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.item}"

# lista de compra


class Inventory(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="static/images/", blank=True)
    toppings = models.ManyToManyField(
        Topping, blank=True, related_name="toppings")
    special = models.BooleanField(default=False)
    customizable = models.BooleanField(default=True)
    item_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True)
    comments = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f" {self.name}"


# precio de compra
class ItemCost(models.Model):
    size = models.ForeignKey(
        Size, on_delete=models.PROTECT, blank=True, null=True)
    itemcost = models.ManyToManyField(
        Inventory, blank=True, related_name="cost")
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        for each in self.itemcost.all():
            return f"{self.size} {each} ${self.amount}"


class ToppingCount(models.Model):
    count = models.CharField(max_length=64)
    inventory = models.ManyToManyField(
        ItemCost, blank=True, related_name="toppingcount")
    amount = models.DecimalField(max_digits=6, null=True, decimal_places=2)

    def __str__(self):
        for each in self.inventory.all():
            return f"topping: {self.count} - {each} - price: {self.amount}"


class Completed_Order_Ids(models.Model):
    order_id = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.order_id}"

# models for orders


class Orderr(models.Model):
    STATUS = [
        ('Initiated', 'Initiated'),
        ('Completed', 'Completed'),
        ('Refunded', 'Refunded')
    ]
    qty = models.IntegerField()
    item = models.ManyToManyField(ItemCost, blank=True, related_name="item")
    item_topping = models.ManyToManyField(
        Topping, blank=True, related_name="item_topping")
    order_id = models.ForeignKey(
        Completed_Order_Ids, on_delete=models.PROTECT, null=True)
    status = models.CharField(
        max_length=64, choices=STATUS, default='Initiated')
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = ['item']

    def __str__(self):
        for each in self.item.all():
            t=[]
            for topp in self.item_topping.all():
                t.append(topp)
            if len(t) == 0: 
                return f"{each} - Total price: ${self.amount}"  
            else:
                return f"{each} - Total price: ${self.amount} - {t}"
