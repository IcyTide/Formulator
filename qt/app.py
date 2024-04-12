import sys


from PySide6.QtGui import QIcon

from qt.components.top import TopWidget
from qt.scripts.top import top_script
from qt.components.equipments import EquipmentsWidget
from qt.scripts.equipments import equipments_script
from qt.components.consumables import ConsumablesWidget
from qt.scripts.consumables import consumables_script
from qt.components.talents import TalentsWidget
from qt.scripts.talents import talents_script
from qt.components.recipes import RecipesWidget
from qt.scripts.recipes import recipes_script
# from qt.components.bonuses import BonusesWidget
# from qt.scripts.bonuses import bonuses_script
from qt.components.dashboard import DashboardWidget
from qt.scripts.dashboard import dashboard_script

from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory, QVBoxLayout, QGridLayout, QWidget, QSizePolicy, \
    QHBoxLayout, QTabWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulator")

        icon = QIcon("qt/assets/icon.ico")
        self.setWindowIcon(icon)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.showMaximized()
        layout = QVBoxLayout(self.central_widget)

        self.top_widget = TopWidget()
        self.bottom_widget = QWidget()
        bottom_layout = QHBoxLayout(self.bottom_widget)
        layout.addWidget(self.top_widget)
        layout.addWidget(self.bottom_widget)

        self.config_widget = QTabWidget()
        self.dashboard_widget = DashboardWidget()
        bottom_layout.addWidget(self.config_widget, 1)
        bottom_layout.addWidget(self.dashboard_widget, 1)

        self.equipments_widget = EquipmentsWidget()
        self.config_widget.addTab(self.equipments_widget, "配装")
        self.consumable_widget = ConsumablesWidget()
        self.config_widget.addTab(self.consumable_widget, "消耗品")
        self.talents_widget = TalentsWidget()
        self.config_widget.addTab(self.talents_widget, "奇穴")
        self.recipes_widget = RecipesWidget()
        self.config_widget.addTab(self.recipes_widget, "秘籍")

        parser = top_script(
            self.top_widget, self.bottom_widget, self.dashboard_widget,
            self.talents_widget, self.recipes_widget, self.equipments_widget, self.consumable_widget,
        )
        equipments = equipments_script(self.equipments_widget)
        consumables = consumables_script(self.consumable_widget)
        talents = talents_script(self.talents_widget)
        recipes = recipes_script(self.recipes_widget)
        dashboard_script(parser, self.dashboard_widget, talents, recipes, equipments, consumables)

        self.bottom_widget.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
