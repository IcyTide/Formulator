from qt.components import ComboWithLabel, SpinWithLabel, RadioWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QTabWidget


class FormationWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.formation = ComboWithLabel("阵法")
        layout.addWidget(self.formation)
        self.core_rate = SpinWithLabel("四重覆盖率", maximum=100)
        layout.addWidget(self.core_rate)
        self.formation_rate = SpinWithLabel("五重覆盖率", maximum=100)
        layout.addWidget(self.formation_rate)


class TeamGainsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.team_gains = {}

        tabs = QTabWidget()
        layout.addWidget(tabs)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "七秀")

        self.team_gains["袖气"] = RadioWithLabel("袖气", "常驻")
        tab_layout.addWidget(self.team_gains["袖气"], 0, 0)

        self.team_gains["左旋右转"] = {
            "stack": SpinWithLabel("左旋右转", "层数", maximum=133)
        }
        tab_layout.addWidget(self.team_gains["左旋右转"]["stack"], 1, 0)
        self.team_gains["泠风解怀"] = {
            "rate": SpinWithLabel("泠风解怀", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["泠风解怀"]["rate"], 2, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "天策")

        self.team_gains["撼如雷"] = RadioWithLabel("撼如雷", "常驻")
        tab_layout.addWidget(self.team_gains["撼如雷"], 0, 0)

        self.team_gains["破风"] = {
            "variety": ComboWithLabel("破风", "种类", ["", "破风", "劲风"])
        }
        tab_layout.addWidget(self.team_gains["破风"]["variety"], 1, 0)

        self.team_gains["乘龙箭"] = {
            "rate": SpinWithLabel("乘龙箭", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["乘龙箭"]["rate"], 2, 0)

        self.team_gains["号令三军"] = {
            "stack": SpinWithLabel("号令三军", "层数", maximum=48)
        }
        tab_layout.addWidget(self.team_gains["号令三军"]["stack"], 3, 0)

        self.team_gains["激雷"] = {
            "rate": SpinWithLabel("激雷", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["激雷"]["rate"], 4, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "少林")

        self.team_gains["立地成佛"] = {
            "rate": SpinWithLabel("立地成佛", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["立地成佛"]["rate"], 0, 0)

        self.team_gains["舍身弘法"] = {
            "stack": SpinWithLabel("舍身弘法", "层数", maximum=36),
            "rate": SpinWithLabel("舍身弘法", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["舍身弘法"]["stack"], 1, 0)
        tab_layout.addWidget(self.team_gains["舍身弘法"]["rate"], 1, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "万花")

        self.team_gains["秋肃"] = RadioWithLabel("秋肃", "常驻")
        tab_layout.addWidget(self.team_gains["秋肃"], 0, 0)

        self.team_gains["皎素"] = {
            "rate": SpinWithLabel("皎素", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["皎素"]["rate"], 1, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "纯阳")

        self.team_gains["碎星辰"] = RadioWithLabel("碎星辰", "常驻")
        tab_layout.addWidget(self.team_gains["碎星辰"], 0, 0)

        self.team_gains["破苍穹"] = RadioWithLabel("破苍穹", "常驻")
        tab_layout.addWidget(self.team_gains["破苍穹"], 1, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "藏剑")

        self.team_gains["剑锋百锻"] = {
            "rate": SpinWithLabel("剑锋百锻", "覆盖", maximum=int(100 / 6))
        }
        tab_layout.addWidget(self.team_gains["剑锋百锻"]["rate"], 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "五毒")

        self.team_gains["仙王蛊鼎"] = {
            "rate": SpinWithLabel("仙王蛊鼎", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["仙王蛊鼎"]["rate"], 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "明教")

        self.team_gains["戒火"] = RadioWithLabel("戒火", "常驻")
        tab_layout.addWidget(self.team_gains["戒火"], 0, 0)

        self.team_gains["朝圣言"] = {
            "stack": SpinWithLabel("朝圣言", "层数", maximum=24),
            "rate": SpinWithLabel("朝圣言", "覆盖", maximum=100),
            "variety": ComboWithLabel("朝圣言", "种类", ["", "朝圣言", "圣浴明心"])
        }
        tab_layout.addWidget(self.team_gains["朝圣言"]["variety"], 1, 0)
        tab_layout.addWidget(self.team_gains["朝圣言"]["stack"], 1, 1)
        tab_layout.addWidget(self.team_gains["朝圣言"]["rate"], 1, 2)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "丐帮")

        self.team_gains["酒中仙"] = RadioWithLabel("酒中仙", "常驻")
        tab_layout.addWidget(self.team_gains["酒中仙"], 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "苍云")

        self.team_gains["虚弱"] = RadioWithLabel("虚弱", "常驻")
        tab_layout.addWidget(self.team_gains["虚弱"], 0, 0)

        self.team_gains["寒啸千军"] = {
            "rate": SpinWithLabel("寒啸千军", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["寒啸千军"]["rate"], 1, 0)

        self.team_gains["振奋"] = {
            "stack": SpinWithLabel("振奋", "层数"),
            "rate": SpinWithLabel("振奋", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["振奋"]["stack"], 2, 0)
        tab_layout.addWidget(self.team_gains["振奋"]["rate"], 2, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "长歌")

        self.team_gains["庄周梦"] = {
            "stack": SpinWithLabel("庄周梦", "层数", maximum=133),
            "rate": SpinWithLabel("庄周梦", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["庄周梦"]["stack"], 0, 0)
        tab_layout.addWidget(self.team_gains["庄周梦"]["rate"], 0, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "霸刀")

        self.team_gains["疏狂"] = {
            "rate": SpinWithLabel("疏狂", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["疏狂"]["rate"], 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "药宗")

        self.team_gains["配伍"] = {
            "rate": SpinWithLabel("配伍", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["配伍"]["rate"], 0, 0)

        # self.team_gains["飘黄"] = {
        #     "rate": SpinWithLabel("飘黄", "覆盖", maximum=int(100 / 6))
        # }
        # tab_layout.addWidget(self.team_gains["飘黄"]["rate"], 1, 0)

        layout.addStretch()

    def __getitem__(self, item):
        return self.team_gains[item]

    def items(self):
        return self.team_gains.items()


class BonusesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.tab = QTabWidget()
        layout.addWidget(self.tab)
        self.formation = FormationWidget()
        self.tab.addTab(self.formation, "阵法")
        self.team_gains = TeamGainsWidget()
        self.tab.addTab(self.team_gains, "团队增益")

        layout.addStretch()
