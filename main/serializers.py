from rest_framework import serializers

from main.models import Menu, Dish, Ingredients


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'


class DishListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name')

    class Meta:
        model = Dish
        fields = ['id', 'title', 'user']


class MenuSerializer(serializers.ModelSerializer):
    dish = serializers.PrimaryKeyRelatedField(queryset=Dish.objects.all(),
                                              write_only=True)

    class Meta:
        model = Menu
        exclude = ['user']

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        return super().create(validated_data)


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        exclude = ['user', ]





