from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        **{skill_id: {} for skill_id in range(29532, 29537 + 1)},
        29548: {}
    }
}
