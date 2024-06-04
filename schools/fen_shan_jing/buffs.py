from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS


class 特效触发(Buff):
    def begin(self, parser):
        parser.refresh_buff(-1, 1, 70)

    def end(self, parser):
        parser.refresh_buff(-1, 1, 70)


class 麟黯(Buff):
    def begin(self, parser):
        parser.refresh_buff(-1, 1, 45)
        parser.refresh_target_buff(-8248, 1)


BUFFS: Dict[int, Union[Buff, dict]] = {
    1428: {
        "buff_name": "军啸",
        "activate": False,
        "attributes": {
            "physical_critical_strike_rate": 400,
            "physical_critical_power_rate": 41
        }
    },
    -1: {
        "buff_name": "怒气",
        "max_stack": 100
    },
    -8248: {
        "buff_name": "虚弱",
        "interval": 400,
        "attributes": {
            "physical_shield_gain": -51
        }
    },
    -9052: {
        "buff_name": "绝刀增伤",
        "interval": 4,
        "gains": {
            13075: {
                "skill_damage_addition": [205, 410, 614, 819] * 2
            }
        }
    },
    8244: {
        "buff_name": "血怒",
        "attributes": {
            "physical_attack_power_gain": 102
        }
    },
    8627: {
        "buff_name": "刀魂",
        "attributes": {
            "physical_attack_power_gain": 154
        }
    },
    17176: {
        "buff_name": "分野",
        "attributes": {
            "all_damage_addition": 51
        }
    },
    8267: {
        "buff_name": "恋战",
        "attributes": {
            "physical_critical_strike_rate": 300,
        }
    },
    14309: {
        "buff_name": "锋鸣",
        "attributes": {
            "physical_overcome_gain": 154
        }
    },
    26212: {
        "buff_name": "麟黯",
    },
    8451: {
        "buff_name": "狂绝",
    },
    26214: {
        "buff_name": "麟光计数",
    },
    27161: {
        "buff_name": "血怒·惊涌",
        "attributes": {
            "physical_attack_power_gain": 102
        }
    },
    # 9889: {
    #     "buff_name": "蔑视",
    #     "attributes": {
    #         "all_shield_ignore": 512
    #     }
    # },
    16957: {
        "buff_name": "单刀赴会·战",
        "attributes": {
            "physical_attack_power_base": [4, 40, 100, 150]
        }
    },
    8474: {
        "buff_class": 特效触发,
        "buff_name": "特效触发"
    }
}

for buff_id, detail in BUFFS.items():
    if buff_class := detail.get("buff_class"):
        BUFFS[buff_id] = buff_class(buff_id)
    else:
        BUFFS[buff_id] = Buff(buff_id)
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    if buff_id not in BUFFS:
        BUFFS[buff_id] = buff
