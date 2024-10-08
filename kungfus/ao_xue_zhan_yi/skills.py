from typing import Dict

from base.skill import Skill

SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            12: dict(channel_interval=27),
            400: {}, 409: {}, 431: {}, 701: {}, 702: {}, 6525: {}, 6526: {}, 14882: {}, 15002: {}, 24898: {}, 25772: {},
            32820: {}, 37618: {}, 36568: {}, 18207: {}, 18208: {}, 18603: {}, 18773: {}, 31031: {},
            401: dict(bind_dots={12461: 1}),
            18591: dict(bind_dots={3442: 1}),
        }
    }
}
