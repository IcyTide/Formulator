from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain

GAINS = {
    # 气涌4%双会套装
    1914: CriticalSet(1439),
    # 万世不竭10%套装
    818: damage_addition_recipe([18649, 18650, 18651, 18652, 18653, 22014], 102),
    # 无界套装
    4602: Gain(),
    # 四象轮回5%橙武
    1520: damage_addition_recipe([896], 51),
    # TODO 太极无极5%橙武
    1521: Gain(),
    # 四象轮回5%小橙武
    1136: critical_strike_recipe([896], 500),
    # 橙武特效
    2418: Gain(),
    # 四象轮回·神兵
    1931: Gain(),
    # 无界特效1
    17300: Gain(),
    # 无界特效2
    17239: Gain(),
    **EQUIPMENT_GAINS,
}
