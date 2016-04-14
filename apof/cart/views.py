from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from cart.models import Cart, CartItem
from restaurant.models import Restaurant, MenuPosition, Size


def show_cart(request, template_name="cart.html"):
    cart = Cart.objects.filter(user=request.user.id, ordered=False)
    if cart:
        ci = CartItem.objects.filter(cart_id=cart[0].id)
    return render_to_response(
        template_name, locals(),
        context_instance=RequestContext(request))


def cart_add(request, restaurant_slug,
             meal_slug, size, template_name="cart.html"):
    nameRestaurant = Restaurant.objects.filter(slug=restaurant_slug)
    meal = MenuPosition.objects.filter(
        slug=meal_slug, restaurant=nameRestaurant[0])
    cart = Cart.objects.filter(user=request.user.id, ordered=False)
    if cart:
        size = Size.objects.filter(size=size, name=meal[0].id)
        ci = CartItem()
        ci.product = size[0]
        ci.quantity = 1
        ci.cart_id = cart[0]
        ci.save()
    else:
        new_cart = Cart()
        new_cart.user = request.user
        new_cart.save()
        size = Size.objects.filter(size=size, name=meal[0].id)
        ci = CartItem()
        ci.product = size[0]
        ci.quantity = 1
        ci.cart_id = new_cart
        ci.save()
    return redirect("/my_cart/")


def cart_remove(request, restaurant_slug,
                meal_slug, size, template_name="cart.html"):
    nameRestaurant = Restaurant.objects.filter(slug=restaurant_slug)
    meal = MenuPosition.objects.filter(
        slug=meal_slug, restaurant=nameRestaurant[0])
    size = Size.objects.filter(size=size, name=meal[0].id)
    ci = CartItem.objects.filter(product=size[0])
    ci.delete()
    return redirect("/my_cart/")


def mod(request, template_name="mod.html"):
    cart = Cart.objects.filter(ordered=False)
    ci = CartItem.objects.filter(cart_id__in=cart).order_by('product')
    return render_to_response(
        template_name, locals(),
        context_instance=RequestContext(request))
