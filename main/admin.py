from django.contrib import admin

from .models import Ingredients, Menu, Dish


# class IngredientsInline(admin.TabularInline):
#     model = Ingredients
#     fields = ['ingredients']
#
#
# class DishAdmin(admin.ModelAdmin):
#     inlines = [IngredientsInline]


admin.site.register(Ingredients)
admin.site.register(Dish)
admin.site.register(Menu)
