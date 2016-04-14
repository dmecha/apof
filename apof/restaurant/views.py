from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import RatingForm, RestaurantForm
from .models import MenuPosition, Restaurant, Rating


def index(request):
    if request.user.is_authenticated():
        restaurantList = Restaurant.objects.all()
        context = {'restaurantList': restaurantList}
        return render(request, 'index.html', context)
    else:
        return HttpResponseRedirect("/login")


def add_res(request):
    if request.user.is_staff:
        form = RestaurantForm(request.POST or None)
        if form.is_valid():
            restaurant = form.save()
            restaurant.save()
            return HttpResponseRedirect("/")
        else:
            form = RestaurantForm()
        context = {
            "form": form
        }
        return render(request, 'form_rest.html', context)


def edit_rest(request, restaurant_slug):
    if request.user.is_staff:
        instance = get_object_or_404(Restaurant, slug=restaurant_slug)
        form = RestaurantForm(request.POST or None, instance=instance)
        if form.is_valid():
            restaurant = form.save()
            restaurant.name = instance.name
            restaurant.address = instance.address
            restaurant.phone_number = instance.phone_number
            restaurant.second_pnumber = instance.second_pnumber
            restaurant.is_active = instance.is_active
            restaurant.save()
            return HttpResponseRedirect("/")
        context = {
            "form": form
        }
        return render(request, 'form_rest.html', context)


def menu(request, restaurant_slug):
    nameRestaurant = Restaurant.objects.filter(slug=restaurant_slug)
    mealList = MenuPosition.objects.filter(restaurant__slug=restaurant_slug)
    context = {
        "title": nameRestaurant[0],
        "menu": mealList
    }
    return render(request, 'menu.html', context=context)


def meal_detail(request, restaurant_slug, meal_slug):
    nameRestaurant = Restaurant.objects.filter(slug=restaurant_slug)
    meal = MenuPosition.objects.filter(slug=meal_slug)

    context = {
        "title": nameRestaurant[0],
        "menu": meal[0],
        "meal_slug": meal_slug
    }
    return render(request, 'meal_detail.html', context=context)


def add_comment(request, restaurant_slug, meal_slug):
    meal = MenuPosition.objects.filter(slug=meal_slug)
    if Rating.objects.filter(meal=meal[0], rate_by=request.user):
        instance = get_object_or_404(
            Rating, meal=meal[0], rate_by=request.user)
        form = RatingForm(request.POST or None, instance=instance)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.rate_by = request.user
            comment.meal = meal[0]
            comment.save()
            return HttpResponseRedirect("/restaurant/"
                                        + restaurant_slug + "/" + meal_slug + "/")
    else:
        form = RatingForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.rate_by = request.user
            comment.meal = meal[0]
            comment.save()
            return HttpResponseRedirect("/restaurant/"
                                        + restaurant_slug + "/" + meal_slug + "/")

    context = {
        "form": form,
    }
    return render(request, "comment_meal.html", context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")
