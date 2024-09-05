from assets.constant import MAX_RECIPE_SKILLS, MAX_RECIPES
from qt.components.recipes import RecipesWidget


class Recipes:
    def __init__(self):
        self.recipes = [[] for _ in range(MAX_RECIPE_SKILLS)]

    def __getitem__(self, item):
        return self.recipes[item]

    def __setitem__(self, key, value):
        self.recipes[key] = value


def recipes_script(recipes_widget: RecipesWidget):
    recipes = Recipes()

    def recipe_update(i):
        widget = recipes_widget[i]

        def inner():
            skill = widget.label.text()
            if selected_items := widget.list.selectedItems():
                while len(selected_items) > MAX_RECIPES:
                    selected_items.pop().setSelected(False)
            recipes[i] = [(skill, item.text()) for item in selected_items]

        return inner

    for n, recipe_widget in enumerate(recipes_widget.values()):
        recipe_widget.list.itemSelectionChanged.connect(recipe_update(n))

    return recipes
