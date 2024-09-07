from typing import Tuple

from base.recipe import *
from general.recipes import equipment

RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        1711: {}
    }
}
RECIPES: list = [equipment.RECIPES, RECIPES]
GENERAL_RECIPES: Dict[Tuple[int, int], Recipe] = {}
for recipes in RECIPES:
    for recipe_class, items in recipes.items():
        for recipe_key, attrs in items.items():
            if not isinstance(recipe_key, tuple):
                recipe_key = (recipe_key, 1)
            GENERAL_RECIPES[recipe_key] = recipe = recipe_class(*recipe_key)
            recipe.set_asset(attrs)
