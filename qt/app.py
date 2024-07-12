import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QTabWidget

from qt.components.bonuses import BonusesWidget
from qt.components.config import ConfigWidget
from qt.components.consumables import ConsumablesWidget
from qt.components.dashboard import DashboardWidget
from qt.components.equipments import EquipmentsWidget
from qt.components.recipes import RecipesWidget
from qt.components.talents import TalentsWidget
from qt.components.top import TopWidget
from qt.scripts.bonuses import bonuses_script
from qt.scripts.config import config_script
from qt.scripts.consumables import consumables_script
from qt.scripts.dashboard import dashboard_script
from qt.scripts.equipments import equipments_script
from qt.scripts.recipes import recipes_script
from qt.scripts.talents import talents_script
from qt.scripts.top import top_script


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulator")

        icon = QIcon("assets/icon.ico")
        self.setWindowIcon(icon)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.top_widget = TopWidget()
        layout.addWidget(self.top_widget, 1)

        self.config_widget = ConfigWidget()
        layout.addWidget(self.config_widget, 1)
        self.config_widget.hide()

        self.bottom_widget = QWidget()
        layout.addWidget(self.bottom_widget, 8)
        self.bottom_widget.hide()

        bottom_layout = QHBoxLayout(self.bottom_widget)
        self.detail_widget = QTabWidget()
        self.dashboard_widget = DashboardWidget()
        bottom_layout.addWidget(self.detail_widget, 1)
        bottom_layout.addWidget(self.dashboard_widget, 1)

        self.equipments_widget = EquipmentsWidget()
        self.detail_widget.addTab(self.equipments_widget, "配装")
        self.consumable_widget = ConsumablesWidget()
        self.detail_widget.addTab(self.consumable_widget, "消耗品")
        self.bonus_widget = BonusesWidget()
        self.detail_widget.addTab(self.bonus_widget, "增益")
        self.talents_widget = TalentsWidget()
        self.detail_widget.addTab(self.talents_widget, "奇穴")
        self.recipes_widget = RecipesWidget()
        self.detail_widget.addTab(self.recipes_widget, "秘籍")

        parser = top_script(
            self.top_widget, self.config_widget, self.bottom_widget,
            self.dashboard_widget, self.talents_widget, self.recipes_widget,
            self.equipments_widget
        )
        config_script(
            parser, self.config_widget,
            self.talents_widget, self.recipes_widget,
            self.equipments_widget, self.consumable_widget, self.bonus_widget
        )
        talents = talents_script(self.talents_widget)
        recipes = recipes_script(self.recipes_widget)
        equipments = equipments_script(self.equipments_widget)
        consumables = consumables_script(self.consumable_widget)
        bonuses = bonuses_script(parser, self.bonus_widget)
        dashboard_script(parser, self.dashboard_widget,
                         talents, recipes, equipments, consumables, bonuses)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
