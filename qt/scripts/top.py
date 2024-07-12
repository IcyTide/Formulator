import copy
import json

from PySide6.QtWidgets import QFileDialog, QWidget

from assets.constant import MAX_RECIPES, MAX_STONE_LEVEL
from qt.components.bonuses import BonusesWidget
from qt.components.config import ConfigWidget
from qt.components.consumables import ConsumablesWidget
from qt.components.dashboard import DashboardWidget
from qt.components.equipments import EquipmentsWidget
from qt.components.recipes import RecipesWidget
from qt.components.talents import TalentsWidget
from qt.components.top import TopWidget
from qt.scripts.config import CONFIG
from schools import SUPPORT_SCHOOLS
from utils.io import serialize, unserialize
from utils.parser import Parser


def top_script(
        top_widget: TopWidget, config_widget: ConfigWidget, bottom_widget: QWidget,
        dashboard_widget: DashboardWidget, talents_widget: TalentsWidget, recipes_widget: RecipesWidget,
        equipments_widget: EquipmentsWidget
):
    parser = Parser()

    def upload_logs():
        file_name = QFileDialog(top_widget, "Choose File").getOpenFileName()
        if not file_name[0]:
            return
        parser(file_name[0])
        top_widget.player_select.set_items(
            [parser.id2name[player_id] for player_id in parser.players], keep_index=True, default_index=0
        )
        top_widget.player_select.show()
        top_widget.save_json.show()
        select_player(None)

    top_widget.upload_log.clicked.connect(upload_logs)

    def save_json():
        result = dict(
            records=serialize(parser.records),
            file_name=parser.file_name,
            start_frame=parser.start_frame,
            end_frame=parser.end_frame,
            id2name=parser.id2name,
            name2id=parser.name2id,
            players={player_id: school.id for player_id, school in parser.players.items()},
            targets=parser.targets,
            select_talents=parser.select_talents,
            select_equipments=parser.select_equipments,
        )
        json.dump(result, open(parser.file_name.split(".jcl")[0] + ".json", "w", encoding="utf-8"), ensure_ascii=False)

    top_widget.save_json.clicked.connect(save_json)

    def load_json():
        file_name = QFileDialog(top_widget, "Choose File").getOpenFileName()
        if not file_name[0]:
            return
        result = json.load(open(file_name[0], encoding="utf-8"))
        result['records'] = unserialize(result['records'])
        for player_id, school_id in result['players'].items():
            result['players'][player_id] = copy.deepcopy(SUPPORT_SCHOOLS[school_id])

        for k, v in result.items():
            setattr(parser, k, v)

        top_widget.player_select.set_items(
            [parser.id2name[player_id] for player_id in parser.players], keep_index=True, default_index=0
        )
        top_widget.player_select.show()
        top_widget.save_json.show()
        select_player(None)

    top_widget.upload_json.clicked.connect(load_json)

    def select_player(_):
        player_name = top_widget.player_select.combo_box.currentText()
        if not player_name:
            return
        player_id = parser.name2id[player_name]
        parser.current_player = player_id
        dashboard_widget.target_select.set_items(
            [""] + [parser.id2name[target_id] for target_id in parser.current_targets],
            keep_index=True, default_index=0
        )
        school = parser.players[player_id]
        """ Update config """
        config_choices = list(CONFIG.get(school.school, {}))
        config_widget.config_select.set_items(config_choices, default_index=-1)
        """ Update dashboard """
        dashboard_widget.duration.set_value(parser.duration)

        """ Update talent options """
        for i, talent_widget in enumerate(talents_widget.values()):
            talents = school.talents[i]
            if i < len(parser.select_talents[player_id]):
                default_index = talents.index(parser.select_talents[player_id][i]) + 1
                talent_widget.set_items(
                    [""] + [school.talent_decoder[talent] for talent in talents], default_index=default_index
                )
            else:
                talent_widget.hide()

        """ Update recipe options """
        for recipe_widget in recipes_widget.values():
            recipe_widget.list.clear()
            recipe_widget.hide()
        if not school.platform:
            for i, (skill, recipes) in enumerate(school.recipes.items()):
                recipes_widget[i].set_label(skill)
                recipes_widget[i].set_items(recipes)
                for n in range(min(MAX_RECIPES, len(recipes))):
                    recipes_widget[i].list.item(n).setSelected(True)
                recipes_widget[i].show()

        """ Update equipment options """
        for label, equipment_widget in equipments_widget.items():
            choices = [""]
            for name, detail in equipment_widget.equipment_json.items():
                if detail['kind'] not in (school.kind, school.major):
                    continue
                if detail['school'] not in ("精简", "通用", school.school):
                    continue
                choices.append(name)
            equipment_widget.equipment.set_items(choices)
            if equipment_widget.enchant:
                equipment_widget.enchant.combo_box.setCurrentIndex(0)
            if equipment_widget.stones_json:
                if not (current_index := equipment_widget.stone_level.combo_box.currentIndex()):
                    current_index = MAX_STONE_LEVEL
                equipment_widget.stone_level.combo_box.setCurrentIndex(current_index)
            if select_equipment := parser.select_equipments[player_id].get(label, {}):
                if equipment := equipment_widget.equipment_mapping.get(select_equipment['equipment']):
                    if equipment in equipment_widget.equipment.items:
                        equipment_widget.equipment.combo_box.setCurrentText(equipment)
                if enchant := equipment_widget.enchant_mapping.get(select_equipment['enchant']):
                    if enchant in equipment_widget.enchant.items:
                        equipment_widget.enchant.combo_box.setCurrentText(enchant)

        config_widget.show()
        bottom_widget.show()

    top_widget.player_select.combo_box.currentTextChanged.connect(select_player)

    return parser
