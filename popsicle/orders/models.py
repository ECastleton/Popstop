# Ingredients and flavors have a many-to-many relationship,
# which means that a flavor can have multilple ingredients while
# an ingredient can be reusued in many flavors.

# See https://docs.djangoproject.com/en/1.10/topics/db/models/#many-to-many-relationships
# for more info

from django.db import models

# TODO: auto-fill date_added when user adds new ingredient or flavor

class Ingredient(models.Model):
    """A Model representing an ingredient.
    An ingredient can be used up to once per flavor Model."""
    ingredient_name = models.CharField(max_length=100)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.ingredient_name

class Flavor(models.Model):
    """A Model representing a popsicle flavor."""
    flavor_name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.flavor_name

class CateringMenu(models.Model):
    """A Model representing a Catering Menu."""
    menu_name = models.CharField(max_length=100)
    flavors = models.ManyToManyField(Flavor)

    # TODO: auto-fill date_created field when user adds new menu
    date_created = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.menu_name
