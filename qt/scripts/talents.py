from qt.components.talents import TalentsWidget

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


def talents_script(talents_widget: TalentsWidget):
    talents = Talents()

    def talent_update(i):
        widget = talents_widget[i]

        def inner(index):
            if talent := widget.combo_box.currentText():
                talents[i] = talent
            else:
                talents[i] = ""

        return inner

    for n, talent_widget in enumerate(talents_widget.values()):
        talent_widget.combo_box.currentIndexChanged.connect(talent_update(n))

    return talents
