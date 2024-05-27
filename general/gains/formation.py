from base.attribute import Attribute
from base.gain import Gain


class FormationGain(Gain):
    gain_attributes: dict = {}
    core_gain_attributes: dict = {}
    rate_gain_attributes: dict = {}

    def __init__(self, rate=0, core_rate=0):
        super().__init__(type(self).__name__)
        self.rate = rate / 100
        self.core_rate = core_rate / 100

    def add_attribute(self, attribute: Attribute):
        for attr, value in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        for attr, value in self.core_gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) + int(value * self.core_rate))
        for attr, value in self.rate_gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) + int(value * self.rate))

    def sub_attribute(self, attribute: Attribute):
        for attr, value in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) - value)
        for attr, value in self.core_gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) - int(value * self.core_rate))
        for attr, value in self.rate_gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) - int(value * self.rate))


class 九音惊弦阵(FormationGain):
    gain_attributes = {
        "magical_attack_power_gain": 50,
        "magical_critical_strike_rate": 300,
        "magical_critical_power_rate": 51,
    }
    core_gain_attributes = {"magical_overcome_gain": 307}
    rate_gain_attributes = {"magical_attack_power_gain": 50}


class 七绝逍遥阵(FormationGain):
    gain_attributes = {
        "magical_attack_power_gain": 51,
        "magical_overcome_gain": 300
    }


class 卫公折冲阵(FormationGain):
    gain_attributes = {
        "physical_attack_power_gain": 50,
        "physical_overcome_gain": 200
    }
    core_gain_attributes = {"strength_gain": 10 * 5}
    rate_gain_attributes = {"physical_attack_power_gain": 51}


class 天鼓雷音阵(FormationGain):
    gain_attributes = {
        "magical_attack_power_gain": 51,
        "strain_rate": 20,
        "magical_overcome_gain": 102
    }
    rate_gain_attributes = {"magical_attack_power_gain": 21 * 5}


class 北斗七星阵(FormationGain):
    gain_attributes = {
        "physical_critical_strike_rate": 300,
        "strain_rate": 20,
        "physical_critical_power_rate": 150
    }
    rate_gain_attributes = {"physical_critical_strike_rate": 100 * 5}


class 九宫八卦阵(FormationGain):
    gain_attributes = {
        "magical_critical_strike_rate": 300,
        "strain_rate": 20,
        "magical_critical_power_rate": 154
    }
    rate_gain_attributes = {"magical_critical_strike_rate": 100 * 5}


class 依山观澜阵(FormationGain):
    gain_attributes = {
        "agility_gain": 30,
        "physical_attack_power_gain": 51,
        "physical_critical_power_rate": 204
    }


class 万蛊噬心阵(FormationGain):
    gain_attributes = {
        "magical_attack_power_gain": 51,
        "magical_critical_strike_rate": 300,
        "magical_critical_power_rate": 102
    }
    core_gain_attributes = {"magical_attack_power_gain": 51}
    rate_gain_attributes = {"magical_overcome_gain": 102}


class 流星赶月阵(FormationGain):
    gain_attributes = {
        "strength_gain": 30,
        "strain_rate": 20,
        "physical_overcome_gain": 205
    }
    rate_gain_attributes = {"physical_critical_strike_rate": 500}


class 千机百变阵(FormationGain):
    gain_attributes = {
        "magical_attack_power_gain": 51,
        "all_shield_ignore": 52,
        "all_critical_power_rate": 150
    }
    rate_gain_attributes = {"all_critical_strike_rate": 500}


class 炎威破魔阵(FormationGain):
    gain_attributes = {
        "magical_attack_power_gain": 51,
        "magical_critical_strike_rate": 300,
    }
    core_gain_attributes = {"magical_critical_power_rate": 200}
    rate_gain_attributes = {"magical_critical_strike_rate": 1000}


class 降龙伏虎阵(FormationGain):
    gain_attributes = {
        "physical_attack_power_gain": 50,
        "physical_overcome_gain": 102
    }
    core_gain_attributes = {"physical_overcome_gain": 306}
    rate_gain_attributes = {"physical_overcome_base": 770 * 5}


class 锋凌横绝阵(FormationGain):
    gain_attributes = {
        "physical_critical_strike_rate": 300,
        "strain_rate": 20,
    }
    core_gain_attributes = {"physical_overcome_gain": 153}
    rate_gain_attributes = {"physical_critical_power_rate": 20 * 5}


class 万籁金弦阵(FormationGain):
    gain_attributes = {
        "magical_critical_strike_rate": 300,
        "strain_rate": 20,
        "magical_attack_power_gain": 102
    }
    core_gain_attributes = {"magical_critical_power_rate": 205}
    rate_gain_attributes = {"magical_critical_strike_rate": 500}


class 霜岚洗锋阵(FormationGain):
    gain_attributes = {
        "physical_attack_power_gain": 50,
        "strain_rate": 20,
        "physical_overcome_gain": 102,
    }
    rate_gain_attributes = {"all_critical_strike_rate": 500}


class 墟海引归阵(FormationGain):
    gain_attributes = {
        "physical_critical_strike_rate": 300,
        "physical_attack_power_gain": 133,
        "physical_overcome_gain": 102
    }
    core_gain_attributes = {"physical_attack_power_gain": 51}


class 龙皇雪风阵(FormationGain):
    gain_attributes = {
        "physical_critical_strike_rate": 300,
        "physical_attack_power_gain": 50,
        "physical_critical_power_rate": 154,
    }
    core_gain_attributes = {"physical_critical_power_rate": 100}
    rate_gain_attributes = {"physical_attack_power_gain": 102}


class 九星游年阵(FormationGain):
    values = [102, 92, 82, 71, 61, 51, 41, 31, 20, 10]
    gain_attributes = {
        "magical_attack_power_gain": 51,
        "strain_rate": 20,
        "magical_critical_power_rate": 100
    }
    core_gain_attributes = {"magical_critical_power_rate": sum(values) / len(values)}
    rate_gain_attributes = {"all_damage_addition": int(154 / 2)}


class 乱暮浊茵阵(FormationGain):
    gain_attributes = {
        "magical_attack_power_gain": 51,
        "all_damage_addition": 31,
        "all_critical_strike_rate": 300
    }


class 横云破锋阵(FormationGain):
    gain_attributes = {
        "physical_attack_power_gain": 50,
        "surplus_base": 1516,
        "physical_overcome_gain": 256
    }
    core_gain_attributes = {"physical_critical_power_rate": 100}


class 苍梧引灵阵(FormationGain):
    gain_attributes = {
        "all_critical_strike_rate": 300,
        "strain_rate": 20,
        "all_damage_addition": 62,
    }
    rate_gain_attributes = {"all_critical_power_rate": 150}


FORMATIONS = {
    "": ["千机百变阵", "苍梧引灵阵"],
    "外功": [
        "卫公折冲阵", "北斗七星阵", "依山观澜阵", "流星赶月阵", "降龙伏虎阵", "锋凌横绝阵", "霜岚洗锋阵", "墟海引归阵",
        "龙皇雪风阵", "横云破锋阵"
    ],
    "内功": [
        "九音惊弦阵", "七绝逍遥阵", "天鼓雷音阵", "九宫八卦阵", "万蛊噬心阵", "炎威破魔阵", "万籁金弦阵", "九星游年阵",
        "乱暮浊茵阵"
    ]
}
# FORMATION_GAIN_NAMES = {
#     "九音惊弦阵": "九音惊弦阵(5%内攻3%内会5%内功会效/5%内攻)",
#     "七绝逍遥阵": "七绝逍遥阵(5%内攻30%内破)",
#     "卫公折冲阵": "卫公折冲阵(5%外攻20%外破/5%外攻)",
#     "天鼓雷音阵": "天鼓雷音阵(5%内攻2%无双10%内破/5*2%内攻)",
#     "北斗七星阵": "北斗七星阵(3%外会2%无双15%外功会效/5*1%外会)",
#     "九宫八卦阵": "九宫八卦阵(3%内会2%无双15%内功会效/5*1%内会)",
#     "依山观澜阵": "依山观澜阵(3%身法5%外攻20%外攻会效)",
#     "万蛊噬心阵": "万蛊噬心阵(5%内攻3%内会10%内功会效/10%内破)",
#     "流星赶月阵": "流星赶月阵(3%力道2%无双20%外破/5%外会)",
#     "千机百变阵": "千机百变阵(5%内攻5%无视15%会效/5%会心)",
#     "炎威破魔阵": "炎威破魔阵(5%内攻3%内会/10%内会)",
#     "降龙伏虎阵": "降龙伏虎阵(5%外攻10%外破/5*770外破)",
#     "锋凌横绝阵": "锋凌横绝阵(3%外会2%无双/5*2%外功会效)",
#     "万籁金弦阵": "万籁金弦阵(3%内会2%无双10%内攻/5*1%内会",
#     "霜岚洗锋阵": "霜岚洗锋阵(5%外攻2%无双10%外破/5%会心)",
#     "墟海引归阵": "墟海引归阵(3%外会10%外攻10%外破)",
#     "龙皇雪风阵": "龙皇雪风阵(3%外会5%外攻15%外功会效/10%外攻)",
#     "九星游年阵": "九星游年阵(5%内攻2%无双10%内功会效/15%伤害增加)",
#     "乱暮浊茵阵": "乱暮浊茵阵(5%内攻3%伤害增加3%会心)",
#     "横云破锋阵": "横云破锋阵(5%外攻1516破招25%外破)",
#     "苍梧引灵阵": "苍梧引灵阵(3%会心2%无双6%伤害增加/15%会效)",
# }

FORMATION_GAINS = {
    formation: globals()[formation]
    for formations in FORMATIONS.values() for formation in formations
}
