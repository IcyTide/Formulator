from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout

from general.gains.consumable import *
from qt.components import ComboWithLabel, RadioWithLabel


class ConsumablesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.activation = RadioWithLabel("启用消耗品", tag=True)
        layout.addWidget(self.activation)
        consumables_layout = QGridLayout()
        layout.addLayout(consumables_layout)
        self.consumables = {}

        self.major_food = ComboWithLabel("辅助类食品", items=[""] + list(MAJOR_FOODS))
        self.consumables['major_food'] = self.major_food
        consumables_layout.addWidget(self.major_food, 0, 0)
        self.minor_food = ComboWithLabel("增强类食品", items=[""] + list(MINOR_FOODS))
        self.consumables['minor_food'] = self.minor_food
        consumables_layout.addWidget(self.minor_food, 0, 1)
        self.major_potion = ComboWithLabel("辅助类药品", items=[""] + list(MAJOR_POTIONS))
        self.consumables['major_potion'] = self.major_potion
        consumables_layout.addWidget(self.major_potion, 1, 0)
        self.minor_potion = ComboWithLabel("增强类药品", items=[""] + list(MINOR_POTIONS))
        self.consumables['minor_potion'] = self.minor_potion
        consumables_layout.addWidget(self.minor_potion, 1, 1)

        self.weapon_enchant = ComboWithLabel("武器磨石", items=[""] + list(WEAPON_ENCHANTS))
        self.consumables['weapon_enchant'] = self.weapon_enchant
        consumables_layout.addWidget(self.weapon_enchant, 2, 0)
        self.home_snack = ComboWithLabel("家园食物", items=[""] + list(SNACKS))
        self.consumables['home_snack'] = self.home_snack
        consumables_layout.addWidget(self.home_snack, 3, 0)
        self.home_wine = ComboWithLabel("家园酒", items=[""] + list(WINES))
        self.consumables['home_wine'] = self.home_wine
        consumables_layout.addWidget(self.home_wine, 3, 1)

        self.guild_spread = ComboWithLabel("帮会宴席", items=[""] + list(GUILD_SPREAD))
        self.consumables['guild_spread'] = self.guild_spread
        consumables_layout.addWidget(self.guild_spread, 4, 0)
        self.guild_food = ComboWithLabel("帮会食物", items=[""] + list(GUILD_FOOD))
        self.consumables['guild_food'] = self.guild_food
        consumables_layout.addWidget(self.guild_food, 4, 1)
        self.spread = ComboWithLabel("宴席", items=[""] + list(SPREADS))
        self.consumables['spread'] = self.spread
        consumables_layout.addWidget(self.spread, 5, 0)
        self.boiled_fish = ComboWithLabel("水煮鱼", items=[""] + list(BOILED_FISH))
        self.consumables['boiled_fish'] = self.boiled_fish
        consumables_layout.addWidget(self.boiled_fish, 5, 1)

        # self.zongzi = ComboWithLabel("端午节粽子")
        # self.consumables['zongzi'] = self.zongzi
        # layout.addWidget(self.zongzi, 3, 0)
        # self.candy = ComboWithLabel("儿童节糖果")
        # self.consumables['candy'] = self.candy
        # layout.addWidget(self.candy, 3, 1)

        layout.addStretch()

    def __getitem__(self, item) -> [ComboWithLabel, RadioWithLabel]:
        return self.consumables[item]

    def items(self):
        return self.consumables.items()
