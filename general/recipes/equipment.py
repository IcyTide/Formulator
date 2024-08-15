from typing import Dict, Union, Tuple

from base.recipe import SkillRecipe, Recipe


GENERAL_RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        17250: {}, 17239: {}
    }
}
RECIPES: Dict[Tuple[int, int], Recipe] = {}
for recipe_class, recipes in GENERAL_RECIPES.items():
    for recipe_key, attrs in recipes.items():
        if not isinstance(recipe_key, tuple):
            recipe_key = (recipe_key, 1)
        recipe = recipe_class(*recipe_key)
        for attr, value in attrs.items():
            setattr(recipe, attr, value)
        recipe.set_asset()
        RECIPES[recipe_key] = recipe
