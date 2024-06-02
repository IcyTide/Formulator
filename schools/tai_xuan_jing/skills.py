from typing import Dict

from base.skill import Damage, DotDamage, DotSkill

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        24454: {}, 24558: {}, 24675: {}, 24676: {}, 24677: {}, 24811: {}, 24812: {}, 24813: {}, 24814: {}, 24821: {},
        24822: {}, 24823: {}, 24824: {}, 24870: {}, 25174: {}, 25512: {}, 25837: {}, 30847: {}, 32886: {}, 33236: {},
        34683: {}, 37311: {}, 37599: {}
    },
    DotDamage: {24846: {"bind_skill": 33588}},
    DotSkill: {33588: {"bind_skill": 24846}},
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
