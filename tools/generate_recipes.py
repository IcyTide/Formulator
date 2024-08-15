from collections import defaultdict

from tqdm import tqdm

from base.recipe import SkillRecipe, DotRecipe
from schools import SUPPORT_SCHOOLS
from tools import *


def prepare_recipes():
    recipes = []
    for school in SUPPORT_SCHOOLS.values():
        for recipe_key, recipe in school.recipes.items():
            if recipe_key in recipes:
                continue
            if isinstance(recipe, SkillRecipe):
                recipes.append(recipe_key)
            elif isinstance(recipe, DotRecipe):
                recipes.append(recipe_key)

    return recipes


RECIPES = prepare_recipes()

SKILL_RECIPE_TAB = read_tab("settings/skill/recipeSkill.tab").fillna(0)
MOBILE_SKILL_RECIPE_TAB = read_tab("settings/skill_mobile/recipeSkill.tab").fillna(0)
SKILL_RECIPE_TAB = pd.concat([SKILL_RECIPE_TAB, MOBILE_SKILL_RECIPE_TAB], axis=0)
BUFF_RECIPE_TAB = read_tab("settings/skill/BuffRecipe.tab").fillna(0)


def parse_skill_recipe(row):
    result = {}
    if damage_addition := row.DamageAddPercent:
        result['damage_addition'] = int(damage_addition)
    if skill_id := row.SkillID:
        result['skill_id'] = int(skill_id)
    if recipe_type := row.SkillRecipeType:
        result['recipe_type'] = int(recipe_type)
    if recipe_mask := row.SkillRecipeTagMask:
        result['recipe_mask'] = int(recipe_mask)
    result['recipe_name'] = row.RecipeName
    return result


def parse_buff_recipe(row):
    result = {}
    if interval := row.IntervalFrameAdd:
        result['interval'] = int(interval)
    if tick := row.CountAdd:
        result['tick'] = int(tick)
    result['buff_id'] = int(row.BuffID)
    result['recipe_name'] = row.RecipeName
    return result


def collect_result():
    results = defaultdict(dict)
    for recipe_id, recipe_level in tqdm(RECIPES):
        if recipe_id > 0:
            filter_recipes = SKILL_RECIPE_TAB[
                (SKILL_RECIPE_TAB.RecipeID == recipe_id) & (SKILL_RECIPE_TAB.RecipeLevel == recipe_level)
            ]
            for _, recipe_row in filter_recipes.iterrows():
                results[recipe_id][recipe_level] = parse_skill_recipe(recipe_row)
        else:
            filter_recipes = BUFF_RECIPE_TAB[
                (BUFF_RECIPE_TAB.RecipeID == -recipe_id) & (BUFF_RECIPE_TAB.RecipeLevel == recipe_level)
            ]
            for _, recipe_row in filter_recipes.iterrows():
                results[recipe_id][recipe_level] = parse_buff_recipe(recipe_row)
    return results


def convert_json(result):
    exclude_columns = ["buff_id", "buff_level"]
    result_json = {}
    for buff_id in result.buff_id.unique().tolist():
        filter_result = result[result.buff_id == buff_id]
        result_json[buff_id] = dict(attributes={}, max_level=int(filter_result.buff_level.max()))
        for column in result.columns:
            if column in exclude_columns:
                continue
            if filter_result[column].isna().all():
                continue

            if filter_result[column].dtype == float:
                filter_column = filter_result[column].fillna(0).astype(int)
            else:
                filter_column = filter_result[column]

            result_dict = result_json[buff_id]
            result_dict[column] = filter_column.tolist()

    save_code("buffs", result_json)


def generate():
    results = collect_result()
    save_code("recipes", results)


if __name__ == '__main__':
    generate()
