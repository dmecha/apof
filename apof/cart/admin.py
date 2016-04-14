from django.contrib import admin

from .models import Cart, CartItem


class CartModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "ordered", "paid", "updated", "timestamp"]

    class Meta:
        model = Cart
admin.site.register(Cart, CartModelAdmin)


class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ["cart_id", "quantity", "product"]

    class Meta:
        model = CartItem
admin.site.register(CartItem, CartItemModelAdmin)
