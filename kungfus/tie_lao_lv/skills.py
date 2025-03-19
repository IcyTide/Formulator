from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    0: {
        Skill: {
            12: dict(channel_interval=27),
            402: {}, 409: {}, 431: {}, 701: {}, 702: {}, 14882: {}, 13778: {}, 32820: {}, 37618: {}, 36568: {},
            18207: {}, 18208: {}, 18603: {}, 18773: {}, 25772: {}, 31031: {}, 24843: {},
            401: dict(bind_dots={12461: 1}),
            18591: dict(bind_dots={3442: 1}),
        }
    }
}
