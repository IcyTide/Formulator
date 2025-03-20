from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 奇穴
        29835: dict(buff_name="度冥"), 18174: {}, 18002: {}, 28303: {}, 28304: {}, 28305: {}, 18176: {}, 18021: {},
    }
}
