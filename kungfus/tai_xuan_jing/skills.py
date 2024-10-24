from typing import Dict

from base.skill import Skill

SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            25512: dict(channel_interval=16), 24454: {}, 24558: {}, 24870: {}, 25233: {}, 25174: {}, 25837: {},
            30847: {}, 32886: {}, 28815: {}, 33236: {}, 34683: {}, 37311: {}, 37599: {}, 33588: {},
            **{skill_id: {} for skill_id in range(24675, 24677 + 1)},
            **{skill_id: {} for skill_id in range(24811, 24814 + 1)},
            **{skill_id: {} for skill_id in range(24821, 24824 + 1)},
        }
    }
}
