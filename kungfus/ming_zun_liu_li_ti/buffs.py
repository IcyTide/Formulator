from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 奇穴
        12578: dict(buff_name="驱夷逐法", begin_frame_shift=-2),
        **{buff_id: dict(buff_name="净体不畏", begin_frame_shift=-2) for buff_id in (30644, 30645)},
        18222: {}
    }
}
