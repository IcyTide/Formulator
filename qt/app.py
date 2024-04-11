import sys


from PySide6.QtGui import QIcon

from qt.components.top import TopWidget
from qt.scripts.top import top_script
from qt.components.equipments import EquipmentsWidget
from qt.scripts.equipments import equipments_script
from qt.components.talents import TalentsWidget
from qt.scripts.talents import talents_script
from qt.components.recipes import RecipesWidget
from qt.scripts.recipes import recipes_script
# from qt.components.consumables import ConsumablesWidget
# from qt.scripts.consumables import consumables_script
# from qt.components.bonuses import BonusesWidget
# from qt.scripts.bonuses import bonuses_script
from qt.components.dashboard import DashboardWidget
from qt.scripts.dashboard import dashboard_script

from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory, QVBoxLayout, QGridLayout, QWidget, QSizePolicy


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
        self.config_widget = QWidget()
        config_layout = QGridLayout(self.config_widget)
        layout.addWidget(self.top_widget)
        layout.addWidget(self.config_widget)

        self.dashboard_widget = DashboardWidget()
        config_layout.addWidget(self.dashboard_widget, 0, 1)
        self.dashboard_widget.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        self.equipments_widget = EquipmentsWidget()
        config_layout.addWidget(self.equipments_widget, 0, 0)
        # self.equipments_widget.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        self.talents_widget = TalentsWidget()
        config_layout.addWidget(self.talents_widget, 1, 0)
        # self.talents_widget.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        self.recipes_widget = RecipesWidget()
        config_layout.addWidget(self.recipes_widget, 2, 0)
        # self.recipes_widget.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        parser = top_script(
            self.top_widget, self.config_widget, self.dashboard_widget,
            self.equipments_widget, self.talents_widget, self.recipes_widget
        )
        equipments = equipments_script(self.equipments_widget)
        talents = talents_script(self.talents_widget)
        recipes = recipes_script(self.recipes_widget)
        dashboard_script(parser, equipments, talents, recipes, self.dashboard_widget)

        # self.talents_widget = TalentsWidget()
        # self.tab_widget.addTab(self.talents_widget, "奇穴")
        #
        # self.recipes_widget = RecipesWidget()
        # self.tab_widget.addTab(self.recipes_widget, "秘籍")
        #
        # self.consumables_widget = ConsumablesWidget()
        # self.tab_widget.addTab(self.consumables_widget, "消耗品")
        #
        # self.bonuses_widget = BonusesWidget()
        # self.tab_widget.addTab(self.bonuses_widget, "增益")
        #
        # self.combat_widget = CombatWidget()
        # self.tab_widget.addTab(self.combat_widget, "战斗")
        #
        # school = top_script(self.top_widget, self.tab_widget,
        #                     self.equipments_widget, self.talents_widget, self.recipes_widget,
        #                     self.consumables_widget, self.bonuses_widget,
        #                     self.combat_widget)
        # equipments = equipments_script(self.equipments_widget)
        # talents = talents_script(self.talents_widget)
        # recipes = recipes_script(self.recipes_widget)
        # consumables = consumables_script(self.consumables_widget)
        # bonuses = bonuses_script(school, self.bonuses_widget)
        # combat_script(self.message_box, school, equipments, talents, recipes, consumables, bonuses, self.combat_widget)

        self.config_widget.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
