"""apof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from restaurant import views
from cart import views as cart_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^my_cart/$', cart_views.show_cart,
        {'template_name': 'cart.html'}, name='show_cart'),

    url(r'^mod/$', cart_views.mod, name='mod'),
    url(r'^mod/add_res/$', views.add_res, name='add_res'),
    url(r'^mod/(?P<restaurant_slug>[-\w]+)/$', views.edit_rest, name='edit_rest'),


    url(r'^my_cart/(?P<restaurant_slug>[-\w]+)/(?P<meal_slug>[-\w]+)/(?P<size>[-\w]+)/add$', cart_views.cart_add, name='cart_add'),
    url(r'^my_cart/(?P<restaurant_slug>[-\w]+)/(?P<meal_slug>[-\w]+)/(?P<size>[-\w]+)/remove$', cart_views.cart_remove, name='cart_remove'),

    url(r'^restaurant/(?P<restaurant_slug>[-\w]+)/$', views.menu, name='menu'),
    url(r'^restaurant/(?P<restaurant_slug>[-\w]+)/(?P<meal_slug>[-\w]+)/$', views.meal_detail, name='meal_detail'),
    url(r'^restaurant/(?P<restaurant_slug>[-\w]+)/(?P<meal_slug>[-\w]+)/comment$', views.add_comment, name='comment_meal'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
