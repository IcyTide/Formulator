from base.attribute import Attribute
from base.gain import Gain
from general.buffs.team import BUFFS


class TeamGain(Gain):
    attributes: dict = {}
    variety_values: dict = {}

    def __init__(self, rate=100, stack=1, variety=None):
        super().__init__()
        self.rate = rate / 100
        self.stack = stack
        self.variety = variety

    def add_attribute(self, attribute: Attribute):
        for attr, value in self.attributes.items():
            value = (value + self.variety_values.get(self.variety, 0))
            setattr(attribute, attr, getattr(attribute, attr) + int(value * self.rate * self.stack))

    def sub_attribute(self, attribute: Attribute):
        for attr, value in self.attributes.items():
            value = value + self.variety_values.get(self.variety, 0)
            setattr(attribute, attr, getattr(attribute, attr) - int(value * self.rate * self.stack))


""" 七秀 """


class 袖气(TeamGain):
    attributes = {"all_major_base": 244}


class 左旋右转(TeamGain):
    attributes = BUFFS[20938].attributes


class 泠风解怀(TeamGain):
    attributes = BUFFS[23573].attributes


""" 天策 """


class 撼如雷(TeamGain):
    attributes = {"physical_attack_power_gain": 51}


class 破风(TeamGain):
    attributes = {"physical_shield_base": -1150}
    variety_values = {"劲风": -1397 + 1150}


class 乘龙箭(TeamGain):
    attributes = {"physical_shield_gain": -102}


class 号令三军(TeamGain):
    attributes = {"strain_base": (500 + 500 / 2) / 2}


class 激雷(TeamGain):
    attributes = {"physical_attack_power_gain": 205, "physical_overcome_gain": 205}


""" 少林 """


class 立地成佛(TeamGain):
    attributes = {"magical_shield_gain": -30 * 5}


class 舍身弘法(TeamGain):
    attributes = {"strain_base": 500}


""" 万花 """


class 秋肃(TeamGain):
    attributes = {"all_damage_cof": 61}


class 皎素(TeamGain):
    attributes = {"all_critical_power_rate": 51}


""" 纯阳 """


class 碎星辰(TeamGain):
    attributes = {"physical_critical_power_rate": 100}


class 破苍穹:
    attributes = {"magical_critical_power_rate": 100}


""" 藏剑 """


class 剑锋百锻(TeamGain):
    attributes = {"weapon_damage_gain": 1536}


""" 五毒 """


class 仙王蛊鼎(TeamGain):
    attributes = {"all_damage_addition": 123}


""" 明教 """


class 戒火(TeamGain):
    attributes = {"all_damage_cof": 21}


class 朝圣言(TeamGain):
    attributes = {"strain_base": 500}
    variety_values = {"圣浴明心": 875 - 500}


""" 丐帮 """


class 酒中仙(TeamGain):
    attributes = {"physical_critical_strike_rate": 100}


""" 苍云 """


class 虚弱(TeamGain):
    attributes = {"physical_shield_gain": -51}


class 振奋(TeamGain):
    attributes = {"physical_overcome_base": 60, "magical_overcome_base": 60}


class 寒啸千军(TeamGain):
    attributes = {"physical_overcome_gain": 204, "magical_overcome_gain": 204}


""" 长歌 """


class 庄周梦(TeamGain):
    attributes = {"strain_base": 50}


class 弄梅(TeamGain):
    attributes = {"all_shield_ignore": 205, "physical_overcome_base": 700, "magical_overcome_base": 700}


""" 霸刀 """


class 疏狂(TeamGain):
    attributes = {"physical_attack_power_gain": 307, "magical_attack_power_gain": 307}


""" 药宗 """


class 配伍(TeamGain):
    attributes = {"all_major_gain": 10 * 5}


TEAM_GAIN_LIMIT = {
    "左旋右转": {
        "stack": 150
    },
    "号令三军": {
        "stack": 48
    },
    "舍身弘法": {
        "stack": 36
    },
    "朝圣言": {
        "stack": 24
    },
    "振奋": {
        "stack": 125
    },
    "庄周梦": {
        "stack": 200
    }
}
TEAM_GAINS = {
    "袖气": 袖气,
    "左旋右转": 左旋右转,
    "泠风解怀": 泠风解怀,

    "撼如雷": 撼如雷,
    "破风": 破风,
    "乘龙箭": 乘龙箭,
    "号令三军": 号令三军,
    "激雷": 激雷,

    "立地成佛": 立地成佛,
    "舍身弘法": 舍身弘法,

    "秋肃": 秋肃,
    "皎素": 皎素,

    "碎星辰": 碎星辰,
    "破苍穹": 破苍穹,

    "剑锋百锻": 剑锋百锻,

    "仙王蛊鼎": 仙王蛊鼎,

    "戒火": 戒火,
    "朝圣言": 朝圣言,

    "酒中仙": 酒中仙,

    "虚弱": 虚弱,
    "振奋": 振奋,
    "寒啸千军": 寒啸千军,

    "庄周梦": 庄周梦,
    "弄梅": 弄梅,

    "疏狂": 疏狂,

    "配伍": 配伍,
}
