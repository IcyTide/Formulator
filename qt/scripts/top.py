from typing import Dict, List

from PySide6.QtWidgets import QTabWidget, QFileDialog, QWidget

from base.buff import Buff
from base.skill import Skill
from general.consumables import FOODS, POTIONS, WEAPON_ENCHANTS, SNACKS, WINES, SPREADS
from qt.components.consumables import ConsumablesWidget
from qt.components.dashboard import DashboardWidget
from qt.components.equipments import EquipmentsWidget
from qt.components.recipes import RecipesWidget
from qt.components.talents import TalentsWidget
from utils.lua import parse
# from qt.components.equipments import EquipmentsWidget
# from qt.components.talents import TalentsWidget
# from qt.components.recipes import RecipesWidget
# from qt.components.consumables import ConsumablesWidget
# from qt.components.bonuses import BonusesWidget
# from qt.components.combat import CombatWidget
from qt.components.top import TopWidget

# from general.consumables import FOODS, POTIONS, WEAPON_ENCHANTS, SPREADS, SNACKS, WINES
# from general.gains.formation import FORMATIONS
from qt.constant import School, SUPPORT_SCHOOL, MAX_RECIPES, MAX_STONE_LEVEL


class Parser:
    records: list
    status: dict

    start_time: list
    end_time: list
    record_index: Dict[str, int]

    fight_flag: bool

    select_talents: List[int]

    school: School | None

    def duration(self, i):
        return round((self.end_time[i] - self.start_time[i]) / 1000, 3)

    def reset(self):
        self.fight_flag = False

        self.records = []
        self.status = {}

        self.start_time = []
        self.end_time = []

        self.record_index = {}

        self.school = None

    def parse_info(self, detail):
        if isinstance(detail, list):
            self.school = SUPPORT_SCHOOL.get(detail[3])
            if not self.school:
                raise AttributeError(f"Cannot support {detail[3]} now")
            self.select_talents = [row[1] for row in detail[6]]
            return self.school

    def parse_time(self, detail, timestamp):
        if detail[1]:
            self.start_time.append(int(timestamp))
            self.records.append({})
            self.fight_flag = True
        else:
            self.end_time.append(int(timestamp))
            self.fight_flag = False

    def parse_buff(self, detail):
        buff_id, buff_stack, buff_level = detail[4], detail[5], detail[8]
        if buff_id not in self.school.buffs:
            return
        if not buff_stack:
            self.status.pop((buff_id, buff_level))
        else:
            self.status[(buff_id, buff_level)] = buff_stack

    def parse_skill(self, detail, timestamp):
        skill = detail[4], detail[5]
        if skill[0] not in self.school.skills:
            return

        current_record = self.records[len(self.start_time) - 1]
        if skill not in current_record:
            current_record[skill] = {}
        status = tuple(
            (buff_id, buff_level, buff_stack) for (buff_id, buff_level), buff_stack in self.status.items()
        )
        if status not in current_record[skill]:
            current_record[skill][status] = []
        current_record[skill][status].append(int(timestamp) - self.start_time[-1])

    def __call__(self, file_name):
        self.reset()
        lines = open(file_name).readlines()
        for line in lines:
            row = line.split("\t")
            if row[4] == "4" and self.parse_info(parse(row[-1])):
                break

        for line in lines:
            row = line.split("\t")
            if row[4] == "5":
                self.parse_time(parse(row[-1]), row[3])
            elif row[4] == "13":
                self.parse_buff(parse(row[-1]))
            elif row[4] == "21" and self.fight_flag:
                self.parse_skill(parse(row[-1]), row[3])

        self.record_index = {
            f"{i + 1}:{round((end_time - self.start_time[i]) / 1000, 3)}": i for i, end_time in enumerate(self.end_time)
        }


def top_script(top_widget: TopWidget, config_widget: QWidget, dashboard_widget: DashboardWidget,
               talents_widget: TalentsWidget, recipes_widget: RecipesWidget,
               equipments_widget: EquipmentsWidget, consumables_widget: ConsumablesWidget
               ):
    parser = Parser()

    def upload_logs():
        file_name = QFileDialog(top_widget, "Choose File").getOpenFileName()
        parser(file_name[0])
        school = parser.school
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

            equipment_widget.equipment.set_items(choices)

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

    top_widget.upload_button.clicked.connect(upload_logs)

    return parser
