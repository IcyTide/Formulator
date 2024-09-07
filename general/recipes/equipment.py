from typing import Dict, Union, Tuple

from base.recipe import SkillRecipe, Recipe

RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        17250: {}, 17239: {}
    }
}
