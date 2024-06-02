from typing import Dict

from base.skill import Skill, Damage, PetDamage, DotDamage, DotSkill, DotConsumeSkill


class 灵蛇引(Skill):
    bind_buffs: list
    skill_name = "灵蛇引"

    def record(self, critical, parser):
        super().record(critical, parser)
        pet_buffs = {(bind_buff, 1): 1 for bind_buff in self.bind_buffs}
        parser.current_next_pet_buff_stacks.append(pet_buffs)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        2183: {}, 3067: {}, 13472: {}, 18590: {}, 25044: {}, 25773: {}, 29573: {}, 30918: {}, 32818: {}, 34389: {}
    },
    PetDamage: {2472: {}, 22997: {}, 36292: {}, 25019: {}},
    DotDamage: {
        6218: {"bind_skill": 13476},
        25917: {"bind_skill": 34643},
        2509: {"bind_skill": 6238},
        2295: {"bind_skill": 6236},
        18882: {"bind_skill": 26226},
    },
    DotSkill: {
        6621: {"bind_skill": 6218},
        34643: {"bind_skill": 25917},
        6238: {"bind_skill": 2509},
        6236: {"bind_skill": 2295},
        26226: {"bind_skill": 18882},
    },
    DotConsumeSkill: {
        34879: {
            "bind_skill": 25917,
            "tick": 99
        }
    },
    灵蛇引: {2223: {"bind_buffs": []}}
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
