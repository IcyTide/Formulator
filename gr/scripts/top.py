import json

import gradio as gr

from general.consumables import FOODS, POTIONS, WEAPON_ENCHANTS, SNACKS, WINES, SPREADS
from general.gains.formation import FORMATIONS
from gr.components.top import TopComponent
from gr.components.equipments import EquipmentsComponent
from gr.components.talents import TalentsComponent
from gr.components.recipes import RecipesComponent
from gr.components.combat import CombatComponent
from assets.constant import MAX_RECIPES, MAX_EMBED_ATTR, MAX_EMBED_LEVEL
from schools import SUPPORT_SCHOOL
from utils.parser import Parser
from utils.io import serialize, unserialize


def top_script(
        top_component: TopComponent, bottom_component: gr.Group,
        equipments_component: EquipmentsComponent,
        talents_component: TalentsComponent, recipes_component: RecipesComponent,
        combat_component: CombatComponent
):
    parser = Parser()

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
        result = json.dumps(result, ensure_ascii=False)
        return result

    def upload_log(file_path):
        if not file_path:
            return [None] * 4
        parser(file_path)
        players = [parser.id2name[player_id] for player_id in parser.players]
        player_select_update = gr.update(choices=players, value=players[0], visible=True)
        json_copy_update = gr.update(value=save_json(), visible=True)
        return player_select_update, json_copy_update, gr.update(visible=True)

    top_component.upload_log.upload(
        upload_log, top_component.upload_log,
        [top_component.player_select, top_component.copy_json, bottom_component], show_progress="full"
    )

    # def load_json(file_path):
    #     if not file_path:
    #         return [None] * 4
    #     result = json.load(open(file_path, encoding="utf-8"))
    #
    #     result['records'] = unserialize(result['records'])
    #     for player_id, school_id in result['players'].items():
    #         result['players'][player_id] = SUPPORT_SCHOOL[school_id]
    #     for k, v in result.items():
    #         setattr(parser, k, v)
    #
    #     json_link = f"/file={save_json()}"
    #
    #     players = [parser.id2name[player_id] for player_id in parser.players]
    #     player_select_update = gr.update(choices=players, value=players[0], visible=True)
    #     return player_select_update, gr.update(visible=True), gr.update(visible=True), gr.update(value=json_link)
    #
    # top_component.upload_json.upload(
    #     load_json, top_component.upload_json,
    #     [top_component.player_select, top_component.save_json, bottom_component, top_component.save_json]
    # )

    def player_select(player_name):
        if not player_name:
            return {}
        player_id = parser.name2id[player_name]
        parser.current_player = player_id
        school = parser.players[player_id]

        top_update = {
            top_component.target_select: gr.update(
                choices=[""] + [parser.id2name[target_id] for target_id in parser.current_targets], visible=True
            ),
            combat_component.combat_duration: gr.update(value=parser.duration, maximum=parser.duration)
        }

        # """ Update config """
        # config_choices = list(CONFIG.get(school.school, {}))
        # config_widget.config_select.set_items(config_choices, default_index=-1)
        # """ Update dashboard """
        # dashboard_widget.duration.set_value(parser.duration)

        """ Update talent options """
        for i, talent_component in enumerate(talents_component.values()):
            choices = [""] + [school.talent_decoder[talent] for talent in school.talents[i]]
            value = school.talent_decoder[parser.select_talents[player_id][i]]
            top_update[talent_component] = gr.update(choices=choices, value=value)

        """ Update recipe options """
        for recipe_component in recipes_component.values():
            top_update[recipe_component] = gr.update(choices=[], visible=False)

        for i, (skill, recipes) in enumerate(school.recipes.items()):
            recipe_component = recipes_component[i]
            values = recipes[:min(MAX_RECIPES, len(recipes))]
            top_update[recipe_component] = gr.update(choices=recipes, value=values, label=skill, visible=True)

        """ Update equipment options """
        for label, equipment_component in equipments_component.items():
            top_update[equipment_component.equipment] = equipment_update = gr.update()
            top_update[equipment_component.enchant] = enchant_update = gr.update()
            top_update[equipment_component.strength_level] = strength_level = gr.update()
            embed_level_updates = [gr.update(value=MAX_EMBED_LEVEL)] * MAX_EMBED_ATTR
            for i, embed_level in enumerate(equipment_component.embed_levels):
                top_update[embed_level] = embed_level_updates[i]

            equipment_update["choices"] = equipment_choices = [""]
            for name, detail in equipment_component.equipment_json.items():
                if detail['kind'] not in (school.kind, school.major):
                    continue
                if detail['school'] not in ("精简", "通用", school.school):
                    continue
                equipment_choices.append(name)
            if select_equipment := parser.select_equipments[player_id].get(label, {}):
                if equipment_name := equipment_component.equipment_mapping.get(select_equipment['equipment']):
                    equipment_update["value"] = equipment_name
                if enchant := equipment_component.enchant_mapping.get(select_equipment['enchant']):
                    enchant_update["value"] = enchant
                strength_level["value"] = select_equipment['strength_level']
                for i, embed_level in enumerate(select_equipment['embed_levels']):
                    embed_level_updates[i] = gr.update(value=embed_level)

        return top_update
        #
        # """ Update consumable options """
        # consumables_widget.major_food.set_items([""] + FOODS[school.major], keep_index=True)
        # consumables_widget.minor_food.set_items([""] + FOODS[school.kind] + FOODS[""], keep_index=True)
        # consumables_widget.major_potion.set_items([""] + POTIONS[school.major], keep_index=True)
        # consumables_widget.minor_potion.set_items([""] + POTIONS[school.kind] + POTIONS[""], keep_index=True)
        # consumables_widget.weapon_enchant.set_items([""] + WEAPON_ENCHANTS[school.kind], keep_index=True)
        # consumables_widget.home_snack.set_items([""] + SNACKS[school.kind] + SNACKS[""], keep_index=True)
        # consumables_widget.home_wine.set_items([""] + WINES[school.major] + WINES[""], keep_index=True)
        # consumables_widget.spread.set_items([""] + SPREADS[school.major] + SPREADS[school.kind], keep_index=True)
        #
        # """ Update bonus options """
        # bonus_widget.formation.formation.set_items([""] + FORMATIONS[school.kind] + FORMATIONS[""], keep_index=True)
        # config_widget.show()
        # bottom_widget.show()

    top_component.player_select.change(
        player_select, top_component.player_select,
        sum([[e.equipment, e.enchant, e.strength_level, *e.embed_levels] for e in equipments_component.values()], []) +
        talents_component.talents + recipes_component.recipes +
        [combat_component.combat_duration] + [top_component.target_select],
    )

    def target_select(target_name):
        target_id = parser.name2id.get(target_name)
        parser.current_target = target_id

    top_component.target_select.change(
        target_select, top_component.target_select
    )

    return parser
