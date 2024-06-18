from typing import Dict

from base.recipe import MagicalCriticalRecipe, DamageAdditionRecipe
from base.talent import Talent

TALENT_GAINS: Dict[int, Talent] = {
    5972: Talent("腾焰飞芒", [
        MagicalCriticalRecipe((1000, 102), skill_id, skill_recipe)
        for skill_id, skill_recipe in ((3963, 0), (3960, 3960))
    ]),
    18279: Talent("净身明礼", [
        DamageAdditionRecipe(256, skill_id, skill_id)
        for skill_id in (3963, 3960)
    ]),
    22888: Talent("诛邪镇魔"),
    6717: Talent("无明业火"),
    34383: Talent("明光恒照"),
    34395: Talent("日月同辉"),
    34372: Talent("靡业报劫"),
    17567: Talent("用晦而明"),
    25166: Talent("净体不畏"),
    5979: Talent("天地诛戮"),
    34378: Talent("降灵尊"),
    34347: Talent("悬象著明"),
    37337: Talent("崇光斩恶"),
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
    [37337]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
