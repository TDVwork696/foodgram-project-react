from enum import Enum


class IngredientInRecipeWrite(Enum):
    MIN_VALUE_VALIDATOR: int = 1
    MAX_VALUE_VALIDATOR: int = 999


class RecipeWriteSerializers(Enum):
    MIN_VALUE_VALIDATOR: int = 1
    MAX_VALUE_VALIDATOR: int = 200
