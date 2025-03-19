from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 奇穴
        **{buff_id: dict(buff_name=f"百节·{i + 1}") for i, buff_id in enumerate((15927, 15928, 15929))},
        15893: {}, 15932: {}, 15832: dict(buff_name="星旗"), 21588: dict(buff_name="孤路")
    }
}
