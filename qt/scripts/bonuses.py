from general.gains import RealBonusGain
from general.gains.formation import FORMATION_GAINS
from general.gains.team import TEAM_GAINS

from qt.components import RadioWithLabel, ComboWithLabel, SpinWithLabel
from qt.components.bonuses import BonusesWidget
from utils.parser import Parser


class Bonuses(dict):
    activate: bool = False

    @property
    def gains(self):
        if not self.activate:
            return []

        gains = list(self.values())
        if "秋肃" in self and "戒火" in self:
            gains.remove(self["戒火"])

        return gains


def bonuses_script(parser: Parser, bonuses_widget: BonusesWidget):
    bonuses = Bonuses()

    def activate_gain():
        widget = bonuses_widget.activation
        if widget.radio_button.isChecked():
            bonuses.activate = True
        else:
            bonuses.activate = False

    bonuses_widget.activation.radio_button.clicked.connect(activate_gain)

    def real_bonus_gain():
        widget = bonuses_widget.real_formulation
        if widget.radio_button.isChecked():
            bonuses[None] = RealBonusGain()
        else:
            bonuses.pop(None, None)

    bonuses_widget.real_formulation.radio_button.clicked.connect(real_bonus_gain)

    def formation_update(_):
        widget = bonuses_widget.formation
        formation = widget.formation.combo_box.currentText()
        rates = [rate.spin_box.value() for rate in widget.rates]
        if formation == parser.current_school.formation:
            widget.rates[0].show()
            widget.rates[-1].show()
        else:
            rates[0] = 0
            widget.rates[0].hide()
            rates[-1] = 0
            widget.rates[-1].hide()

        if formation:
            bonuses['formation'] = FORMATION_GAINS[formation](rates)
        else:
            bonuses.pop("formation", None)

    bonuses_widget.formation.formation.combo_box.currentTextChanged.connect(formation_update)
    for rate_widget in bonuses_widget.formation.rates:
        rate_widget.spin_box.valueChanged.connect(formation_update)

    def radio_update(label):
        widget = bonuses_widget.team_gains[label]

        def inner():
            if widget.radio_button.isChecked():
                bonuses[label] = TEAM_GAINS[label]()
            else:
                bonuses.pop(label, None)

        return inner

    def combine_update(label):
        widgets = bonuses_widget.team_gains[label]

        def inner(_):
            kwargs = {}
            for attr, widget in widgets.items():
                if isinstance(widget, ComboWithLabel):
                    kwargs[attr] = widget.combo_box.currentText()
                elif isinstance(widget, SpinWithLabel):
                    kwargs[attr] = widget.spin_box.value()
            if all(kwargs.values()):
                bonuses[label] = TEAM_GAINS[label](**kwargs)
            else:
                bonuses.pop(label, None)

        return inner

    for bonus_label, bonus_widget in bonuses_widget.team_gains.items():
        if isinstance(bonus_widget, RadioWithLabel):
            bonus_widget.radio_button.clicked.connect(radio_update(bonus_label))
        elif isinstance(bonus_widget, dict):
            for sub_bonus_widget in bonus_widget.values():
                if isinstance(sub_bonus_widget, ComboWithLabel):
                    sub_bonus_widget.combo_box.currentTextChanged.connect(combine_update(bonus_label))
                elif isinstance(sub_bonus_widget, SpinWithLabel):
                    sub_bonus_widget.spin_box.valueChanged.connect(combine_update(bonus_label))
                else:
                    raise TypeError
        else:
            raise TypeError

    bonuses_widget.team_gains.set_default()

    return bonuses
