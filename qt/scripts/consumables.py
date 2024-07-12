from general.gains.consumable import CONSUMABLES
from qt.components.consumables import ConsumablesWidget


class Consumables(dict):
    activate: bool = True

    @property
    def attrs(self):
        if not self.activate:
            return {}
        final_attrs = {}
        for consumable in self.values():
            for attr, value in consumable.items():
                if attr not in final_attrs:
                    final_attrs[attr] = 0
                final_attrs[attr] += value
        return final_attrs


def consumables_script(consumables_widget: ConsumablesWidget):
    consumables = Consumables()

    def activate_gain():
        widget = consumables_widget.activation
        if widget.radio_button.isChecked():
            consumables.activate = True
        else:
            consumables.activate = False

    consumables_widget.activation.radio_button.clicked.connect(activate_gain)

    def consumable_update(label):
        widget = consumables_widget[label]

        def inner(index):
            consumable = widget.combo_box.currentText()
            if consumable:
                consumables[label] = CONSUMABLES[consumable]
            else:
                consumables[label] = {}

        return inner

    for consumable_label, consumable_widget in consumables_widget.items():
        consumable_widget.combo_box.currentTextChanged.connect(consumable_update(consumable_label))

    return consumables
