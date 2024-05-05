from django.contrib.auth import get_user_model
from django.core.validators import (MinValueValidator, MaxValueValidator,
                                    RegexValidator)
from django.db import models
from django.db.models import UniqueConstraint

from .constants import Ingredient, Tag, Recipes, IngredientInRecipes

User = get_user_model()


class Ingredient(models.Model):
    """ Модель Ингридиентов """

    name = models.CharField('Название',
                            max_length=Ingredient.NAME_LEN)
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=Ingredient.MEASUREMENT_UNIT_LEN)

    class Meta:
        unique_together = ('name', 'measurement_unit')
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    """ Модель Тэгов """

    name = models.CharField('Название', unique=True,
                            max_length=Tag.TAG_NAME_LEN)
    color = models.CharField(
        'Цветовой HEX-код',
        unique=True,
        max_length=Tag.COLOR_LEN,
        validators=[
            RegexValidator(
                regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
                message='Введенное значение не является цветом в формате HEX!'
            )
        ]
    )
    slug = models.SlugField(
        'Уникальный слаг', unique=True, max_length=Tag.SLUG_LEN)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """ Модель Рецепта """

    name = models.CharField(
        'Название', max_length=Recipes.NAME_LEN)
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
    )
    text = models.TextField('Описание')
    image = models.ImageField(
        'Изображение',
        upload_to='recipes/'
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        validators=[MinValueValidator(
            Recipes.COOKING_TIME_MIN_VALUE,
            message='Минимальное значение '
            f'{Recipes.COOKING_TIME_MIN_VALUE}!'),
            MaxValueValidator(
                Recipes.COOKING_TIME_MAX_VALUE,
                message='Максимальное значение '
                f'< {Recipes.COOKING_TIME_MAX_VALUE}!')]
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    """ Модель для связи Ингридиента и Рецепта """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    amount = models.PositiveSmallIntegerField(
        'Количество',
        validators=[MinValueValidator(
            IngredientInRecipes.AMOUNT_MIN_VALUE,
            message='Минимальное количество '
            f'{IngredientInRecipes.AMOUNT_MIN_VALUE}!'),
            MaxValueValidator(
                IngredientInRecipes.AMOUNT_MAX_VALUE,
                message='Максимальное значение < '
                f'{IngredientInRecipes.AMOUNT_MAX_VALUE}!')]
    )

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'

    def __str__(self):
        return (
            f'{self.ingredient.name}'
            f'({self.ingredient.measurement_unit}) - {self.amount} '
        )


class FavouriteShoppingCartModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )

    class Meta:
        abstract = True


class Favourite(FavouriteShoppingCartModel):
    """ Модель Избранные """
    class Meta(FavouriteShoppingCartModel.Meta):
        default_related_name = 'favorites'
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'], name='unique_favourite')
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Избранное'


class ShoppingCart(FavouriteShoppingCartModel):
    """ Модель Корзина покупок """
    class Meta(FavouriteShoppingCartModel.Meta):
        default_related_name = 'shopping_cart'
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзина покупок'
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'], name='unique_shopping_cart')
        ]

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Корзину покупок'
