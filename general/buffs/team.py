from base.buff import Buff

GENERAL_BUFFS = {
    15413: {
        "buff_name": "基础攻击",
        "gain_attributes": {
            "physical_attack_power_base": [0] * 8 + [371, 450, 495, 549],
            "magical_attack_power_base": [0] * 8 + [442, 538, 591, 655]
        }
    },
    20938: {
        "buff_name": "左旋右转",
        "gain_attributes": {
            "surplus_base": 54,
        }
    },
    23573: {
        "buff_name": "泠风解怀",
        "gain_attributes": {
            "all_damage_addition": 154
        }
    },
    3465: {
        "buff_name": "破甲",
        "gain_attributes": {
            "physical_shield_gain": -102
        }
    },
    23107: {
        "buff_name": "号令三军",
        "gain_attributes": {
            "strain_base": 500
        }
    },
    6363: {
        "buff_name": "激雷",
        "gain_attributes": {
            "physical_attack_power_gain": 205, "physical_overcome_gain": 205
        }
    },
    10208: {
        "buff_name": "弘法",
        "gain_attributes": {
            "strain_base": 500
        }
    },
    24350: {
        "buff_name": "皎素",
        "gain_attributes": {
            "all_critical_power_gain": 51
        }
    },
    24742: {
        "buff_name": "仙王蛊鼎",
        "gain_attributes": {
            "all_damage_addition": 123
        }
    },
    4246: {
        "buff_name": "朝圣",
        "gain_attributes": {
            "strain_base": 500
        }
    },
    9744: {
        "buff_name": "朝圣",
        "gain_attributes": {
            "strain_base": 875
        }
    },
    8504: {
        "buff_name": "振奋",
        "gain_attributes": {
            "physical_overcome_base": 60,
            "magical_overcome_base": 60
        }
    },
    10031: {
        "buff_name": "寒啸千军",
        "gain_attributes": {
            "physical_overcome_gain": 204,
            "magical_overcome_gain": 204
        }
    },
    23543: {
        "buff_name": "庄周梦",
        "gain_attributes": {
            "strain_base": 50
        }
    },
    16911: {
        "buff_name": "弄梅",
        "gain_attributes": {
            "physical_overcome_base": 700,
            "magical_overcome_base": 700,
            "all_shield_ignore": 205
        }
    },
    11456: {
        "buff_name": "疏狂",
        "gain_attributes": {
            "physical_attack_power_gain": 307,
            "magical_attack_power_gain": 307
        }
    },
    20877: {
        "buff_name": "配伍",
        "gain_attributes": {
            "all_major_gain": 10
        }
    }
}

for buff_id, detail in GENERAL_BUFFS.items():
    GENERAL_BUFFS[buff_id] = Buff(buff_id)
    GENERAL_BUFFS[buff_id].activate = False
    for attr, value in detail.items():
        setattr(GENERAL_BUFFS[buff_id], attr, value)
