from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        14083: {},
        # 奇穴
        29344: {}, 30396: {}, 13966: {}, 29348: dict(buff_name="鸿轨"),
        14321: dict(buff_name="驰行")
    }
}
