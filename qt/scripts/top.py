import copy
import json

from PySide6.QtWidgets import QFileDialog, QWidget

from assets.constant import MAX_RECIPES, MAX_STONE_LEVEL
from assets.dot_bind_skills import DOT_BIND_SKILLS
from assets.dot_buffs import DOT_BUFFS
from assets.school_buffs import SCHOOL_BUFFS
from assets.skill_buffs import SKILL_BUFFS
from general.skills import GENERAL_SKILLS
from qt.components.config import ConfigWidget
from qt.components.dashboard import DashboardWidget
from qt.components.equipments import EquipmentsWidget
from qt.components.recipes import RecipesWidget
from qt.components.talents import TalentsWidget
from qt.components.top import TopWidget
from qt.scripts.config import CONFIG
from schools import SUPPORT_SCHOOLS
from utils.analyzer import Analyzer
from utils.io import serialize, unserialize


def top_script(
        top_widget: TopWidget, config_widget: ConfigWidget, detail_widget: QWidget,
        equipments_widget: EquipmentsWidget, talents_widget: TalentsWidget, recipes_widget: RecipesWidget,
        dashboard_widget: DashboardWidget
):
    analyzer = Analyzer()

    # def save_json():
    #     result = dict(
    #         records=serialize(parser.records),
    #         file_name=parser.file_name,
    #         start_frame=parser.start_frame,
    #         end_frame=parser.end_frame,
    #         id2name=parser.id2name,
    #         name2id=parser.name2id,
    #         players={player_id: school.id for player_id, school in parser.players.items()},
    #         targets=parser.targets,
    #         select_talents=parser.select_talents,
    #         select_equipments=parser.select_equipments,
    #     )
    #     json.dump(result, open(parser.file_name.split(".jcl")[0] + ".json", "w", encoding="utf-8"), ensure_ascii=False)
    #
    # top_widget.save_json.clicked.connect(save_json)
    #
    # def load_json():
    #     file_name = QFileDialog(top_widget, "Choose File").getOpenFileName()
    #     if not file_name[0]:
    #         return
    #     result = json.load(open(file_name[0], encoding="utf-8"))
    #     result['records'] = unserialize(result['records'])
    #     for player_id, school_id in result['players'].items():
    #         result['players'][player_id] = copy.deepcopy(SUPPORT_SCHOOLS[school_id])
    #
    #     for k, v in result.items():
    #         setattr(parser, k, v)
    #
    #     top_widget.player_select.set_items(
    #         [parser.id2name[player_id] for player_id in parser.players], keep_index=True, default_index=0
    #     )
    #     top_widget.player_select.show()
    #     top_widget.save_json.show()
    #     select_player(None)
    #
    # top_widget.upload_json.clicked.connect(load_json)

    def select_school(_):
        school_name = top_widget.school_select.combo_box.currentText()
        if not school_name:
            return
        school = SUPPORT_SCHOOLS[school_name]
        analyzer.school = school
        """ Update config """
        config_choices = list(CONFIG.get(school.name, {}))
        config_widget.config_select.set_items(config_choices, default_index=-1)

        """ Update talent options """
        for i, talent_widget in enumerate(talents_widget.values()):
            talent_choices = school.talent_choices[i]
            talent_widget.set_items([""] + [school.talent_decoder[talent] for talent in talent_choices])

        """ Update recipe options """
        for recipe_widget in recipes_widget.values():
            recipe_widget.list.clear()
            recipe_widget.hide()
        for i, (skill, recipes) in enumerate(school.recipe_choices.items()):
            recipes_widget[i].set_label(skill)
            recipes_widget[i].set_items(recipes)
            for n in range(min(MAX_RECIPES, len(recipes))):
                recipes_widget[i].list.item(n).setSelected(True)
            recipes_widget[i].show()

        """ Update equipment options """
        for label, equipment_widget in equipments_widget.items():
            choices = [""]
            for name, detail in equipment_widget.equipment_data.items():
                if detail['kind'] not in (school.kind, school.major):
                    continue
                if detail['school'] not in ("精简", "通用", school.school):
                    continue
                choices.append(name)
            equipment_widget.equipment.combo_box.clear()
            equipment_widget.equipment.set_items(choices)
            if equipment_widget.enchant:
                equipment_widget.enchant.combo_box.setCurrentIndex(0)
            if equipment_widget.stones_data:
                if not (current_index := equipment_widget.stone_level.combo_box.currentIndex()):
                    current_index = MAX_STONE_LEVEL
                equipment_widget.stone_level.combo_box.setCurrentIndex(current_index)

        """ Update dashboard options """
        dashboard_widget.buff_select.buff_id_select.set_items(
            [str(buff_id) for buff_id in SCHOOL_BUFFS[school.id]], default_index=-1
        )
        if dashboard_widget.damage_select.damage_type_radio.radio_button.isChecked():
            damage_ids = [str(dot_id) for dot_id in DOT_BIND_SKILLS[school.id]]
        else:
            damage_ids = [str(skill_id) for skill_id in SKILL_BUFFS[school.id]]
        dashboard_widget.damage_select.damage_id_select.set_items(damage_ids, default_index=-1)

        config_widget.show()
        detail_widget.show()

    top_widget.school_select.combo_box.currentTextChanged.connect(select_school)

    return analyzer
