from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            24553: {}, 24209: {}, 24557: {},
            24179: dict(buff_name="雨积"),
            24180: dict(buff_name="镇机")
        }
    },
    1: {
        Buff: {
            71297: {}
        }
    }
}
