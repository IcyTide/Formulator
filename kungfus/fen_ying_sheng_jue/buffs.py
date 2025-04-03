from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 奇穴
        28886: {}, 4754: {}, 6277: {}, 25759: dict(buff_name="明光·日"), 25758: dict(buff_name="明光·月"),
        30642: {}, 30643: {}, 30644: {}, 30645: {}, -12575: dict(buff_name="用晦而明")
    }
}
