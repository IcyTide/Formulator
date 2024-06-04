from typing import Dict

from base.skill import Skill, Damage, PetDamage, DotDamage


class 灵蛇引(Skill):
    bind_buffs: list
    skill_name = "灵蛇引"

    def record(self, critical, parser):
        super().record(critical, parser)
        pet_buffs = {(bind_buff, 1): 1 for bind_buff in self.bind_buffs}
        parser.current_next_pet_buff_stacks.append(pet_buffs)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        2183: dict(damage_addition=205), 
        3067: {}, 13472: {}, 18590: {}, 25044: {}, 25773: {}, 29573: {}, 30918: {}, 32818: {}, 34389: {},
    },
    PetDamage: {2472: {}, 22997: {}, 36292: {}, 25019: {}},
    DotDamage: {
        6218: {}, 2509: {}, 2295: {}, 18882: {},
        25917: dict(extra_tick=1),
    },
    Skill: {
        13476: dict(bind_dot=6218),
        34643: dict(bind_dot=25917),
        6238: dict(bind_dot=2509),
        6236: dict(bind_dot=2295),
        26226: dict(bind_dot=18882),
        34879: dict(consume_dot=25917)
    },
    灵蛇引: {2223: dict(bind_buffs=[16543])}
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
