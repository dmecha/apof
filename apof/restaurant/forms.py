from django import forms
from django.utils.text import slugify
from .models import Rating, Restaurant


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            "comment",
            "ratings"
        ]


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            "name",
            "address",
            "phone_number",
            "second_pnumber",
            "is_active"
        ]

    def save(self):
        instance = super(RestaurantForm, self).save()
        instance.slug = slugify(instance.name)
        instance.save()

        return instance
