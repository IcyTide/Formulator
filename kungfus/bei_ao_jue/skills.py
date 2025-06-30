from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        **{skill_id: dict(channel_interval=24) for skill_id in (16419, 16820, 16822)}, 32823: {},
        # 殷雷腿
        16599: {}, 16631: {}, **{skill_id: {} for skill_id in (16097, 16753, 16774, 16775)},
        # 秀明尘身
        20991: {}, **{skill_id: {} for skill_id in (16758, 16759, 16760, 16382)},
        **{skill_id: {} for skill_id in (16800, 16801, 16802, 16803, 16804, 17043, 19423, 19424)},
        # 松烟竹雾
        17092: {}, **{skill_id: dict(bind_dots={11447: 1}) for skill_id in (17058, 17060)},
        **{skill_id: {} for skill_id in range(16933, 16944 + 1)},
        # 雪絮金屏
        16794: {}, **{skill_id: {} for skill_id in range(16787, 16791 + 1)},
        **{skill_id: {} for skill_id in range(16610, 16614 + 1)},
        **{skill_id: {} for skill_id in range(16615, 16619 + 1)},
        # 奇穴
        38533: {}, 37984: {}, 38537: {}, 34585: {},
        # 装备
        25782: {}, 39106: {}, 21933: {}, 21999: {}
    }
}
