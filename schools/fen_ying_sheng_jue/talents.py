from typing import Dict

from base.gain import Gains
from base.recipe import MagicalCriticalRecipe, DamageAdditionRecipe

TALENT_GAINS: Dict[int, Gains] = {
    5972: Gains("腾焰飞芒", [
        MagicalCriticalRecipe((1000, 102), skill_id, skill_recipe)
        for skill_id, skill_recipe in ((3963, 0), (3960, 3960))
    ]),
    18279: Gains("净身明礼", [
        DamageAdditionRecipe(256, skill_id, skill_id)
        for skill_id in (3963, 3960)
    ]),
    22888: Gains("诛邪镇魔"),
    6717: Gains("无明业火"),
    34383: Gains("明光恒照"),
    34395: Gains("日月同辉"),
    34372: Gains("靡业报劫"),
    17567: Gains("用晦而明"),
    25166: Gains("净体不畏"),
    5979: Gains("天地诛戮"),
    34378: Gains("降灵尊"),
    34347: Gains("悬象著明"),
    37337: Gains("崇光斩恶"),
    34370: Gains("日月齐光")
}

TALENTS = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
