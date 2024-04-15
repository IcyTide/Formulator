from PySide6.QtWidgets import QFileDialog, QWidget

from general.consumables import FOODS, POTIONS, WEAPON_ENCHANTS, SNACKS, WINES, SPREADS
from qt.components.config import ConfigWidget
from qt.components.consumables import ConsumablesWidget
from qt.components.dashboard import DashboardWidget
from qt.components.equipments import EquipmentsWidget
from qt.components.recipes import RecipesWidget
from qt.components.talents import TalentsWidget
from qt.components.top import TopWidget

# from general.consumables import FOODS, POTIONS, WEAPON_ENCHANTS, SPREADS, SNACKS, WINES
# from general.gains.formation import FORMATIONS
from qt.constant import MAX_RECIPES, MAX_STONE_LEVEL
from qt.scripts.config import CONFIG
from utils.parser import Parser


def top_script(top_widget: TopWidget, config_widget: ConfigWidget, bottom_widget: QWidget,
               dashboard_widget: DashboardWidget, talents_widget: TalentsWidget, recipes_widget: RecipesWidget,
               equipments_widget: EquipmentsWidget, consumables_widget: ConsumablesWidget):
    parser = Parser()

    def upload_logs():
        file_name = QFileDialog(top_widget, "Choose File").getOpenFileName()
        parser(file_name[0])
        school = parser.school
        """ Update config """
        config_choices = list(CONFIG.get(school.school, {}))
        config_widget.config_select.set_items(config_choices, default_index=-1)
        """ Update dashboard """
        record_index = list(parser.record_index)
        dashboard_widget.fight_select.set_items(record_index)
        dashboard_widget.duration.set_value(parser.duration(parser.record_index[record_index[0]]))

        """ Update talent options """
        for i, talent_widget in enumerate(talents_widget.values()):
            talents = school.talents[i]
            default_index = talents.index(parser.select_talents[i]) + 1
            talent_widget.set_items([""] + [school.talent_decoder[talent] for talent in talents],
                                    default_index=default_index)

        """ Update recipe options """
        for recipe_widget in recipes_widget.values():
            recipe_widget.list.clear()
            recipe_widget.hide()

        for i, (skill, recipes) in enumerate(school.recipes.items()):
            recipes_widget[i].set_label(skill)
            recipes_widget[i].set_items(recipes)
            for n in range(MAX_RECIPES):
                recipes_widget[i].list.item(n).setSelected(True)
            recipes_widget[i].show()

        """ Update equipment options """
        for equipment_widget in equipments_widget.values():
            choices = [""]
            for name, detail in equipment_widget.equipment_json.items():
                if detail['kind'] not in (school.kind, school.major):
                    continue
                if detail['school'] not in ("精简", "通用", school.school):
                    continue
                choices.append(name)
            current_equipment = equipment_widget.equipment.combo_box.currentText()
            if current_equipment in choices:
                default_index = choices.index(current_equipment)
            else:
                default_index = -1
            equipment_widget.equipment.set_items(choices, default_index=default_index)

            if equipment_widget.stones_json:
                equipment_widget.stone_level.combo_box.setCurrentIndex(MAX_STONE_LEVEL)

        """ Update consumable options """
        consumables_widget.major_food.set_items([""] + FOODS[school.major])
        consumables_widget.minor_food.set_items([""] + FOODS[school.kind] + FOODS[""])
        consumables_widget.major_potion.set_items([""] + POTIONS[school.major])
        consumables_widget.minor_potion.set_items([""] + POTIONS[school.kind] + POTIONS[""])
        consumables_widget.weapon_enchant.set_items([""] + WEAPON_ENCHANTS[school.kind])
        consumables_widget.home_snack.set_items([""] + SNACKS[school.kind] + SNACKS[""])
        consumables_widget.home_wine.set_items([""] + WINES[school.major] + WINES[""])
        consumables_widget.spread.set_items([""] + SPREADS[school.major] + SPREADS[school.kind])

        config_widget.show()
        bottom_widget.show()

    top_widget.upload_button.clicked.connect(upload_logs)

    return parser
