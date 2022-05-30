from django.contrib.auth import get_user_model
from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='dishs'
    )
    ingredients = models.ManyToManyField(Ingredients)

    def __str__(self):
        return self.title


class Menu(models.Model):
    dish = models.ForeignKey(Dish,
                             on_delete=models.CASCADE,
                             related_name='menu')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='menu')
    created_at = models.DateTimeField(auto_now_add=True)
