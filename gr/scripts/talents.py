from gr.components.talents import TalentsComponent

from assets.constant import MAX_TALENTS


class Talents:
    def __init__(self):
        self.talents = ["" for _ in range(MAX_TALENTS)]

    def __getitem__(self, item):
        return self.talents[item]

    def __setitem__(self, key, value):
        self.talents[key] = value

    @property
    def gains(self):
        return [talent for talent in self.talents if talent]


def talents_script(talents_component: TalentsComponent):
    talents = Talents()

    def talent_changed(i):
        def inner(talent):
            talents[i] = talent

        return inner

    for n, talent_component in enumerate(talents_component.values()):
        talent_component.change(talent_changed(n), talent_component)

    return talents
