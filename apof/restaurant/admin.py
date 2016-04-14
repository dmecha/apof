from django.contrib import admin

from .models import (Ingerents,
                     MenuPosition,
                     Rating,
                     Restaurant,
                     Size)


class IngerentsModelAdmin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = Ingerents
admin.site.register(Ingerents, IngerentsModelAdmin)


class MenuPositionModelAdmin(admin.ModelAdmin):
    list_display = ["restaurant", "name"]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = MenuPosition
admin.site.register(MenuPosition, MenuPositionModelAdmin)


class RatingModelAdmin(admin.ModelAdmin):
    list_display = ["meal", "rate_by", "comment", "ratings"]

    class Meta:
        model = Rating
admin.site.register(Rating, RatingModelAdmin)


class RestaurantModelAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "address",
                    "phone_number", "second_pnumber", "is_active"]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Restaurant
admin.site.register(Restaurant, RestaurantModelAdmin)


class SizeModelAdmin(admin.ModelAdmin):
    list_display = ["name", "size", "price"]
    list_editable = ["price"]

    class Meta:
        model = Size
admin.site.register(Size, SizeModelAdmin)
