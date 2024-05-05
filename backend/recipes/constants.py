class Ingredient:
    NAME_LEN: int = 200
    MEASUREMENT_UNIT_LEN: int = 200


class Tag:
    TAG_NAME_LEN: int = 200
    COLOR_LEN: int = 7
    SLUG_LEN: int = 200


class Recipes:
    NAME_LEN: int = 200
    COOKING_TIME_MIN_VALUE: int = 1
    COOKING_TIME_MAX_VALUE: int = 200


class IngredientInRecipes:
    AMOUNT_MIN_VALUE: int = 1
    AMOUNT_MAX_VALUE: int = 999
