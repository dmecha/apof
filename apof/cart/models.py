from django.conf import settings
from django.db import models
from restaurant.models import Size


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    ordered = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def get_cart_items(self):
        return CartItem.objects.filter(cart_id=self.id)

    def total(self):
        total = 0
        ci = CartItem.objects.filter(cart_id=self.id)
        for x in ci:
            total += x.price
        return total

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Size, unique=False)

    class Meta:
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.product.name

    def get_price(self):
        return self.product.price

    def get_size(self):
        return self.product.get_sizes()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

    def __str__(self):
        return str(self.product)

    price = property(total)
    size = property(get_size)
