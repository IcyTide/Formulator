from gr.components.recipes import RecipesComponent

from assets.constant import MAX_RECIPE_SKILLS


class Recipes:
    def __init__(self):
        self.recipes = [[] for _ in range(MAX_RECIPE_SKILLS)]

    def __getitem__(self, item):
        return self.recipes[item]

    def __setitem__(self, key, value):
        self.recipes[key] = value

    @property
    def gains(self):
        return self.recipes


def recipes_script(recipes_component: RecipesComponent):
    recipes = Recipes()

    def recipe_changed(i):
        def inner(recipe_list):
            if recipe_list:
                recipes[i] = recipe_list
            else:
                recipes[i] = []

        return inner

    for n, recipe_component in enumerate(recipes_component.values()):
        recipe_component.change(recipe_changed(n), recipe_component)

    return recipes
