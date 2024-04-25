from enum import IntEnum


class Ingredient(IntEnum):
    NAME_LEN: int = 200
    MEASUREMENT_UNIT_LEN: int = 200


class Tag(IntEnum):
    TAG_NAME_LEN: int = 200
    COLOR_LEN: int = 7
    SLUG_LEN: int = 200


class Recipes(IntEnum):
    NAME_LEN: int = 200
    MIN_VALUE_VALIDATOR_COOKING_TIME: int = 1
    MAX_VALUE_VALIDATOR_COOKING_TIME: int = 200


class IngredientInRecipes(IntEnum):
    MIN_VALUE_VALIDATOR_AMOUNT: int = 1
    MAX_VALUE_VALIDATOR_AMOUNT: int = 999
