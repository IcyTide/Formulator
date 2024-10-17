from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            20680: {}, 20696: {}, 20054: {},
            20718: dict(buff_name="炮阳"),
            21168: dict(buff_name="植物温性", continuous=True),
            21856: dict(buff_name="荆障"),
            20699: dict(buff_name="养荣"),
            24659: dict(buff_name="应理与药")
        }
    },
    1: {
        Buff: {
            71230: {}, 71258: {}
        }
    }
}
