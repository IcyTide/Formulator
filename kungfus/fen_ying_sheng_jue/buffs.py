from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 奇穴
        28886: {}, 4754: {}, 6277: {}, 25759: dict(buff_name="明光·日"), 25758: dict(buff_name="明光·月"),
        30642: dict(end_frame_shift=2), 30643: dict(end_frame_shift=2), -12575: dict(buff_name="用晦而明")
    }
}
