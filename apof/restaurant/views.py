from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


from .models import MenuPosition, Restaurant


def index(request):

    restaurantList = Restaurant.objects.all()
    context = {'restaurantList': restaurantList}
    return render(request, 'index.html', context)


def menu(request, pk):
    nameRestaurant = Restaurant.objects.filter(pk=pk)
    mealList = MenuPosition.objects.filter(restaurant__pk=pk)
    context = {
        "title": nameRestaurant[0],
        "menu": mealList
    }
    return render(request, 'menu.html', context=context)


def meal_detail(request, pk, meal_id):
    nameRestaurant = Restaurant.objects.filter(pk=pk)
    meal = MenuPosition.objects.filter(id=meal_id)

    context = {
        "title": nameRestaurant[0],
        "menu": meal[0]
    }
    return render(request, 'meal_detail.html', context=context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")
