# Ingredients and flavors have a many-to-many relationship,
# which means that a flavor can have multilple ingredients while
# an ingredient can be reusued in many flavors.

# See https://docs.djangoproject.com/en/1.10/topics/db/models/#many-to-many-relationships
# for more info

from datetime import timedelta
from django.db import models
from django.utils import timezone

class Ingredient(models.Model):
    """A Model representing an ingredient.
    An ingredient can be used up to once per flavor Model."""
    ingredient_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(editable=False)

    def __str__(self):
        return self.ingredient_name

    def save(self, *args, **kwargs):
        """Set date_added field to current time on save.

        Based from http://stackoverflow.com/a/1737078"""
        if not self.id:
            self.date_added = timezone.now()
        return super(Ingredient, self).save(*args, **kwargs)

class Subingredient(models.Model):
    """A Model representing a subingredient. Use only with Ingredient Model"""
    name = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    """A Model representing a product category (i.e. group of flavors)."""
    category_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(editable=False)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ["category_name"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        """Set date_added field to current time on save."""
        if not self.id:
            self.date_added = timezone.now()
        return super(ProductCategory, self).save(*args, **kwargs)

    def get_flavors(self):
        """Returns list of flavors in a category."""
        return list(self.flavor_set.all())

class Flavor(models.Model):
    """A Model representing a flavor."""
    flavor_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default="")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
        default=0)
    ingredients = models.ManyToManyField(Ingredient)
    date_added = models.DateTimeField(editable=False)

    class Meta:
        ordering = ["flavor_name"]

    def save(self, *args, **kwargs):
        """Set date_added field to current time on save"""
        if not self.id:
            self.date_added = timezone.now()
        return super(Flavor, self).save(*args, **kwargs)

    def __str__(self):
        return self.flavor_name

    def ingredients_list(self):
        """Used in admin page for now"""
        ingredients_list = [str(i) for i in self.ingredients.all()]
        return sorted(ingredients_list)

    def is_new_flavor(self):
        """"Returns true if the flavor was added in the last 7 days"""
        one_week_ago = timezone.now() - timedelta(days=7)
        return self.date_added < one_week_ago

class CateringMenu(models.Model):
    """A Model representing a Catering Menu."""
    menu_name = models.CharField(max_length=100)
    flavors = models.ManyToManyField(Flavor)

    date_created = models.DateTimeField(editable=False)
    # TODO: On save, check dates if:
    #       - start_date is earlier than end_date
    #       - difference between start_date and end_date is at least 24 hours
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ["-start_date"] # Sort by most recent date first

    def save(self, *args, **kwargs):
        """Set date_created field to current time on save."""
        if not self.id:
            self.date_created = timezone.now()
        return super(CateringMenu, self).save(*args, **kwargs)

    def __str__(self):
        return self.menu_name

    def is_active(self):
        """Returns True if current date is within the range of start_date
        and end_date."""
        now = timezone.now().date()
        return self.start_date <= now <= self.end_date

    is_active.boolean = True
