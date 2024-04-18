from qt.components import ComboWithLabel, RadioWithLabel
from qt.components.consumables import ConsumablesWidget

from general.consumables import CONSUMABLES


class Consumables(dict):
    @property
    def attrs(self):
        final_attrs = {}
        for consumable in self.values():
            for attr, value in consumable.items():
                if attr not in final_attrs:
                    final_attrs[attr] = 0
                final_attrs[attr] += value
        return final_attrs


def consumables_script(consumables_widget: ConsumablesWidget):
    consumables = Consumables()

    def consumable_combo_update(label):
        widget = consumables_widget[label]

        def inner(index):
            consumable = widget.combo_box.currentText()
            if consumable:
                consumables[label] = CONSUMABLES[consumable]
            else:
                consumables[label] = {}

        return inner

    def consumable_radio_update(label):
        widget = consumables_widget[label]

        def inner():
            if widget.radio_button.isChecked():
                consumables[label] = CONSUMABLES[label]
            else:
                consumables[label] = {}

        return inner

    for consumable_label, consumable_widget in consumables_widget.items():

        if isinstance(consumable_widget, ComboWithLabel):
            consumable_widget.combo_box.currentTextChanged.connect(consumable_combo_update(consumable_label))
        elif isinstance(consumable_widget, RadioWithLabel):
            consumable_widget.radio_button.clicked.connect(consumable_radio_update(consumable_label))

    return consumables
