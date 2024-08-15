from typing import Dict

from base.gain import Gains
from base.recipe import MagicalCriticalRecipe, DamageAdditionRecipe

TALENTS: Dict[int, Gain] = {
    5972: Gain("腾焰飞芒", [
        MagicalCriticalRecipe((1000, 102), skill_id, skill_recipe)
        for skill_id, skill_recipe in ((3963, 0), (3960, 3960))
    ]),
    18279: Gain("净身明礼", [
        DamageAdditionRecipe(256, skill_id, skill_id)
        for skill_id in (3963, 3960)
    ]),
    22888: Gain("诛邪镇魔"),
    6717: Gain("无明业火"),
    34383: Gain("明光恒照"),
    34395: Gain("日月同辉"),
    34372: Gain("靡业报劫"),
    17567: Gain("用晦而明"),
    25166: Gain("净体不畏"),
    5979: Gain("天地诛戮"),
    34378: Gain("降灵尊"),
    34347: Gain("悬象著明"),
    37337: Gain("崇光斩恶"),
    34370: Gain("日月齐光")
}

TALENT_CHOICES = [
    [5972],
    [18279],
    [22888],
    [6717],
    [34383],
    [34395],
    [34372],
    [17567],
    [25166, 5979],
    [34378],
    [34347],
    [37337, 34370]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
