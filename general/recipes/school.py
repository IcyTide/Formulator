from typing import Dict, Union, Tuple

from base.recipe import SkillRecipe, Recipe

GENERAL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        1711: {}
    }
}
RECIPES: Dict[Tuple[int, int], Recipe] = {}
for recipe_class, recipes in GENERAL_RECIPES.items():
    for recipe_key, attrs in recipes.items():
        if not isinstance(recipe_key, tuple):
            recipe_key = (recipe_key, 1)
        RECIPES[recipe_key] = recipe = recipe_class(*recipe_key)
        recipe.set_asset(attrs)
