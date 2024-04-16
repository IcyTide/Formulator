import json
import os

from qt.components.config import ConfigWidget
from qt.components.equipments import EquipmentsWidget
from utils.parser import Parser


if not os.path.exists("config"):
    CONFIG = {}
else:
    CONFIG = json.load(open("config", encoding="utf-8"))


def config_script(parser: Parser, config_widget: ConfigWidget, equipments_widget: EquipmentsWidget):
    def load_config():
        config_name = config_widget.config_select.combo_box.currentText()
        config = CONFIG.get(parser.school.school, {}).get(config_name, {})
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

        config_widget.config_name.text_browser.setText(config_name)

    config_widget.load_config.clicked.connect(load_config)

    def save_config():
        config_name = config_widget.config_name.text_browser.text()
        if parser.school.school not in CONFIG:
            CONFIG[parser.school.school] = {}
        if config_name not in CONFIG[parser.school.school]:
            CONFIG[parser.school.school][config_name] = {}
        config = CONFIG[parser.school.school][config_name]

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
        json.dump(CONFIG, open("config", "w", encoding="utf-8"), ensure_ascii=False)

        config_choices = list(CONFIG.get(parser.school.school, {}))
        if current_select := config_widget.config_select.combo_box.currentText():
            default_index = config_choices.index(current_select)
        else:
            default_index = -1
        config_widget.config_select.set_items(config_choices, default_index=default_index)

    config_widget.save_config.clicked.connect(save_config)
