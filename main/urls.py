from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import IngredientsListView, DishViewSet, MenuViewSet

router = DefaultRouter()
router.register('dishs', DishViewSet)
router.register('menu', MenuViewSet)

urlpatterns = [
    path('ingredients/', IngredientsListView.as_view()),
    path('', include(router.urls))
]
