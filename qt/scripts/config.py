import json
import os

from qt.components import ComboWithLabel, RadioWithLabel, SpinWithLabel
from qt.components.bonuses import BonusesWidget
from qt.components.config import ConfigWidget
from qt.components.equipments import EquipmentsWidget
from qt.components.consumables import ConsumablesWidget
from qt.components.recipes import RecipesWidget
from qt.components.talents import TalentsWidget
from utils.parser import Parser

if not os.path.exists("config"):
    CONFIG = {}
else:
    CONFIG = json.load(open("config", encoding="utf-8"))


def config_script(
        parser: Parser, config_widget: ConfigWidget,
        talent_widget: TalentsWidget, recipe_widget: RecipesWidget,
        equipments_widget: EquipmentsWidget, consumable_widget: ConsumablesWidget, bonus_widget: BonusesWidget):
    def load_equipments(config):
        if not config:
            return

        for label, equipment in equipments_widget.items():
            if 'equipment' not in config[label]:
                continue
            else:
                index = equipment.equipment.combo_box.findText(config[label]['equipment'])
                equipment.equipment.combo_box.setCurrentIndex(index)

            equipment.strength_level.combo_box.setCurrentIndex(config[label]['strength_level'])
            if 'enchant' in config[label]:
                index = equipment.enchant.combo_box.findText(config[label]['enchant'])
                equipment.enchant.combo_box.setCurrentIndex(index)
            if 'special_enchant' in config[label]:
                if equipment.special_enchant.radio_button.isChecked() != config[label]['special_enchant']:
                    equipment.special_enchant.radio_button.click()
            if 'embed_levels' in config[label]:
                for i, embed_level in enumerate(equipment.embed_levels):
                    embed_level.combo_box.setCurrentIndex(config[label]['embed_levels'][i])
            if 'stone_level' in config[label]:
                equipment.stone_level.combo_box.setCurrentIndex(config[label]['stone_level'])
            if 'stone_attrs' in config[label]:
                for i, stone_attr in enumerate(equipment.stone_attrs):
                    index = equipment.stone_attrs[i].combo_box.findText(config[label]['stone_attrs'][i])
                    stone_attr.combo_box.setCurrentIndex(index)

    def load_consumables(config):
        for label, consumable in consumable_widget.items():
            if isinstance(consumable, ComboWithLabel):
                consumable.combo_box.setCurrentText(config[label])
            elif isinstance(consumable, RadioWithLabel):
                if consumable.radio_button.isChecked() != config[label]:
                    consumable.radio_button.click()

    def load_bonuses(config):
        bonus_widget.formation.formation.combo_box.setCurrentText(config['formation']['formation'])
        bonus_widget.formation.core_rate.spin_box.setValue(config['formation']['core_rate'])
        bonus_widget.formation.rate.spin_box.setValue(config['formation']['rate'])
        for label, team_gain in bonus_widget.team_gains.items():
            if isinstance(team_gain, RadioWithLabel):
                if team_gain.radio_button.isChecked() != config['team_gains'][label]:
                    team_gain.radio_button.click()
            elif isinstance(team_gain, dict):
                for sub_label, sub_team_gain in team_gain.items():
                    if isinstance(sub_team_gain, ComboWithLabel):
                        sub_team_gain.combo_box.setCurrentText(config['team_gains'][label][sub_label])
                    elif isinstance(sub_team_gain, SpinWithLabel):
                        sub_team_gain.spin_box.setValue(config['team_gains'][label][sub_label])

    def load_recipes(config):
        for i, recipes in enumerate(config):
            for selected_item in recipe_widget.recipes[i].list.selectedItems():
                selected_item.setSelected(False)

    def load_config():
        config_name = config_widget.config_select.combo_box.currentText()
        config = CONFIG.get(parser.school.school, {}).get(config_name, {})
        if not config:
            return
        category = config_widget.config_category.combo_box.currentText()
        if category == "全部":
            load_equipments(config.get("equipments"))
            load_consumables(config.get("consumables"))
            load_bonuses(config.get("bonuses"))
        elif category == "装备":
            load_equipments(config.get("equipments"))
        elif category == "消耗品":
            load_consumables(config.get("consumables"))
        elif category == "增益":
            load_bonuses(config.get("bonuses"))

        config_widget.config_name.text_browser.setText(config_name)

    config_widget.load_config.clicked.connect(load_config)

    def save_equipments(config):
        for label, equipment in equipments_widget.items():
            config[label] = {}
            if not (text := equipment.equipment.combo_box.currentText()):
                continue
            else:
                config[label]['equipment'] = text
            config[label]['strength_level'] = equipment.strength_level.combo_box.currentIndex()
            if equipment.enchant:
                config[label]['enchant'] = equipment.enchant.combo_box.currentText()
            if equipment.special_enchant:
                config[label]['special_enchant'] = equipment.special_enchant.radio_button.isChecked()
            if equipment.embed_levels:
                config[label]['embed_levels'] = [
                    embed_level.combo_box.currentIndex() for embed_level in equipment.embed_levels
                ]
            if equipment.stone_level:
                config[label]['stone_level'] = equipment.stone_level.combo_box.currentIndex()
            if equipment.stone_attrs:
                config[label]['stone_attrs'] = [
                    stone_attr.combo_box.currentText() for stone_attr in equipment.stone_attrs
                ]

    def save_consumables(config):
        for label, consumable in consumable_widget.items():
            if isinstance(consumable, ComboWithLabel):
                config[label] = consumable.combo_box.currentText()
            elif isinstance(consumable, RadioWithLabel):
                config[label] = consumable.radio_button.isChecked()

    def save_bonuses(config):
        config['formation']['formation'] = bonus_widget.formation.formation.combo_box.currentText()
        config['formation']['core_rate'] = bonus_widget.formation.core_rate.spin_box.value()
        config['formation']['rate'] = bonus_widget.formation.rate.spin_box.value()
        for label, team_gain in bonus_widget.team_gains.items():
            if isinstance(team_gain, RadioWithLabel):
                config['team_gains'][label] = team_gain.radio_button.isChecked()
            elif isinstance(team_gain, dict):
                config['team_gains'][label] = {}
                for sub_label, sub_team_gain in team_gain.items():
                    if isinstance(sub_team_gain, ComboWithLabel):
                        config['team_gains'][label][sub_label] = sub_team_gain.combo_box.currentText()
                    elif isinstance(sub_team_gain, SpinWithLabel):
                        config['team_gains'][label][sub_label] = sub_team_gain.spin_box.value()

    def save_recipes(config):
        for recipe in recipe_widget.values():
            if selected_items := recipe.list.selectedItems():
                config.append(selected_items)

    def save_config():
        config_name = config_widget.config_name.text_browser.text()
        if parser.school.school not in CONFIG:
            CONFIG[parser.school.school] = {}
        if config_name not in CONFIG[parser.school.school]:
            CONFIG[parser.school.school][config_name] = {
                "equipments": {},
                "consumables": {},
                "bonuses": {"formation": {}, "team_gains": {}},
                "talents": [],
                "recipes": []
            }

        save_equipments(CONFIG[parser.school.school][config_name]['equipments'])
        save_consumables(CONFIG[parser.school.school][config_name]['consumables'])
        save_bonuses(CONFIG[parser.school.school][config_name]['bonuses'])
        # save_recipes(CONFIG[parser.school.school][config_name]['recipes'])
        json.dump(CONFIG, open("config", "w", encoding="utf-8"), ensure_ascii=False)

        config_widget.config_select.set_items(
            list(CONFIG.get(parser.school.school, {})), keep_index=True, default_index=-1
        )

    config_widget.save_config.clicked.connect(save_config)

    def delete_config():
        config_name = config_widget.config_name.text_browser.text()
        if config_name not in CONFIG.get(parser.school.school, {}):
            return

        CONFIG[parser.school.school].pop(config_name)

        json.dump(CONFIG, open("config", "w", encoding="utf-8"), ensure_ascii=False)

        config_widget.config_select.set_items(list(CONFIG.get(parser.school.school, {})), default_index=-1)
        config_widget.config_name.text_browser.clear()

    config_widget.delete_config.clicked.connect(delete_config)
