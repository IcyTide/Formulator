import gradio as gr

from assets.constant import MAX_RECIPE_SKILLS, MAX_RECIPES


class RecipesComponent:
    def __init__(self):

        self.recipes = []

        columns = 6
        rows = MAX_RECIPE_SKILLS // columns

        for i in range(rows):
            with gr.Row():
                for j in range(columns):
                    recipe = gr.Dropdown(multiselect=True, max_choices=MAX_RECIPES, visible=False)
                    self.recipes.append(recipe)

    def __getitem__(self, item) -> gr.Dropdown:
        return self.recipes[item]

    def values(self) -> list[gr.Dropdown]:
        return self.recipes
