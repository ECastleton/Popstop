from django.db import models

class Flavor(models.Model):
    flavor_name = models.CharField(max=100)

    def __str__(self):
        return self.flavor_name

class Ingredient(models.Model):
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max=100)

    def __str__(self):
        return self.ingredient_name
