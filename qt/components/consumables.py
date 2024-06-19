from PySide6.QtWidgets import QWidget, QGridLayout

from general.consumables import BOILED_FISH, GUILD_FOOD, GUILD_SPREAD
from qt.components import ComboWithLabel, RadioWithLabel


class ConsumablesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)

        self.consumables = {}

        self.major_food = ComboWithLabel("辅助类食品")
        self.consumables['major_food'] = self.major_food
        layout.addWidget(self.major_food, 0, 0)
        self.minor_food = ComboWithLabel("增强类食品")
        self.consumables['minor_food'] = self.minor_food
        layout.addWidget(self.minor_food, 0, 1)
        self.major_potion = ComboWithLabel("辅助类药品")
        self.consumables['major_potion'] = self.major_potion
        layout.addWidget(self.major_potion, 0, 2)
        self.minor_potion = ComboWithLabel("增强类药品")
        self.consumables['minor_potion'] = self.minor_potion
        layout.addWidget(self.minor_potion, 0, 3)

        self.weapon_enchant = ComboWithLabel("武器磨石")
        self.consumables['weapon_enchant'] = self.weapon_enchant
        layout.addWidget(self.weapon_enchant, 1, 0)
        self.home_snack = ComboWithLabel("家园食物")
        self.consumables['home_snack'] = self.home_snack
        layout.addWidget(self.home_snack, 1, 1)
        self.home_wine = ComboWithLabel("家园酒")
        self.consumables['home_wine'] = self.home_wine
        layout.addWidget(self.home_wine, 1, 2)

        self.guild_spread = RadioWithLabel("同泽宴", GUILD_SPREAD)
        self.consumables['guild_spread'] = self.guild_spread
        layout.addWidget(self.guild_spread, 2, 0)
        self.guild_food = RadioWithLabel("蒸鱼餐盘", GUILD_FOOD)
        self.consumables['guild_food'] = self.guild_food
        layout.addWidget(self.guild_food, 2, 1)
        self.spread = ComboWithLabel("宴席")
        self.consumables['spread'] = self.spread
        layout.addWidget(self.spread, 2, 2)
        self.boiled_fish = ComboWithLabel("水煮鱼", items=[""] + BOILED_FISH[""])
        self.consumables['boiled_fish'] = self.boiled_fish
        layout.addWidget(self.boiled_fish, 2, 3)

        # self.zongzi = ComboWithLabel("端午节粽子")
        # self.consumables['zongzi'] = self.zongzi
        # layout.addWidget(self.zongzi, 3, 0)
        # self.candy = ComboWithLabel("儿童节糖果")
        # self.consumables['candy'] = self.candy
        # layout.addWidget(self.candy, 3, 1)

    def __getitem__(self, item) -> [ComboWithLabel, RadioWithLabel]:
        return self.consumables[item]

    def items(self):
        return self.consumables.items()
