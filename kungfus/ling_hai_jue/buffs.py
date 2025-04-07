from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        30396: {},
        # 奇穴
        29344: {}, 14083: {}, 29348: dict(buff_name="鸿轨"), 14321: dict(buff_name="驰行"), 13966: {},
    }
}
