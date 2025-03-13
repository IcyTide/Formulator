from collections import defaultdict

from tqdm import tqdm

from kungfus import SUPPORT_KUNGFU
from tools import *


def prepare_recipes():
    recipes = []
    for kungfu in SUPPORT_KUNGFU.values():
        for recipe_key in kungfu.recipes:
            if recipe_key in recipes:
                continue
            recipes.append(recipe_key)

    return recipes


SKILL_RECIPE_TAB = read_tab("settings/skill/recipeSkill.tab").fillna(0)
MOBILE_SKILL_RECIPE_TAB = read_tab("settings/skill_mobile/recipeSkill.tab").fillna(0)
SKILL_RECIPE_TAB = pd.concat([SKILL_RECIPE_TAB, MOBILE_SKILL_RECIPE_TAB], axis=0)
BUFF_RECIPE_TAB = read_tab("settings/skill/BuffRecipe.tab").fillna(0)


def parse_skill_recipe(row):
    result = {}
    if damage_addition := row.DamageAddPercent:
        result['damage_addition'] = int(damage_addition)
    if prepare_frame := row.PrepareFramesAdd:
        result['prepare_frame'] = int(prepare_frame)
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
    for recipe_id, recipe_level in tqdm(prepare_recipes()):
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


def generate():
    results = collect_result()
    save_code("recipes", results)


if __name__ == '__main__':
    generate()
