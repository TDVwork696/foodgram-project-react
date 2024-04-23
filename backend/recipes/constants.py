from enum import Enum


class Ingredient(Enum):
    INGREDIENT_NAME_LEN: int = 200
    MEASUREMENT_UNIT_LEN: int = 200


class Tag(Enum):
    TAG_NAME_LEN: int = 200
    COLOR_LEN: int = 7
    SLUG_LEN: int = 200


class Recipe(Enum):
    RECIPE_NAME_LEN: int = 200
    MIN_VALUE_VALIDATOR: int = 1
    MAX_VALUE_VALIDATOR: int = 200


class IngredientInRecipe(Enum):
    MIN_VALUE_VALIDATOR: int = 1
    MAX_VALUE_VALIDATOR: int = 999
