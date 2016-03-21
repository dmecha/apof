from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


WEEKDAYS = [
    (1, ("Poniedziałek")),
    (2, ("Wtorek")),
    (3, ("Środa")),
    (4, ("Czwartek")),
    (5, ("Piątek")),
    (6, ("Sobota")),
    (7, ("Niedziela")),
]

SIZES_OF_MEAL = [
    (1, ('Mała')),
    (2, ('Średnia')),
    (3, ('Duza')),

]


class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Ingerents(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class MenuPosition(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=128)
    ingerents = models.ManyToManyField(Ingerents, max_length=128, blank=True)

    def get_ratings(self):
        return Rating.objects.filter(meal=self.id)

    def get_avgrate(self):
        rates = Rating.objects.filter(meal=self.id)
        if rates:
            counter = len(rates)
            suma = 0
            for rate in rates:
                suma += rate.ratings
            return round((suma / counter), 2)

    def get_sizes(self):
        return Size.objects.filter(name=self.id)

    def __str__(self):
        return str(self.restaurant) + " " + self.name


class Rating(models.Model):

    meal = models.ForeignKey(MenuPosition)
    rate_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.CharField(max_length=128, default="")
    ratings = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (("meal", "rate_by"),)

    def __str__(self):
        return str(self.meal)


class Size(models.Model):

    name = models.ForeignKey(MenuPosition)
    size = models.IntegerField(default=1, choices=SIZES_OF_MEAL)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (("name", "size"),)
        ordering = ['name', 'size']

    def __str__(self):
        return str(self.name) + " " + str(self.price)
