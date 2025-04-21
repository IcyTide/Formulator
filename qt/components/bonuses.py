from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QTabWidget

from base.buff import Buff
from general.buffs import GENERAL_BUFFS
from general.gains.formation import FORMATION_GAINS
from general.gains.team import TEAM_GAINS
from qt.components import ComboWithLabel, SpinWithLabel, RadioWithLabel


class FormationWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        self.formation = ComboWithLabel("阵法", items=[""] + list(FORMATION_GAINS))
        layout.addWidget(self.formation)
        self.rates = []
        self.rates.append(SpinWithLabel("四重覆盖(%)", maximum=100))
        layout.addWidget(self.rates[-1])
        self.rates[-1].hide()
        self.rates.append(SpinWithLabel("五重覆盖(%)", maximum=100))
        layout.addWidget(self.rates[-1])
        self.rates.append(SpinWithLabel("六重覆盖(%)", maximum=100))
        layout.addWidget(self.rates[-1])
        self.rates[-1].hide()


class TeamGainsWidget(QWidget):
    def create_single(self, gain_name):
        self.team_gains[gain_name] = RadioWithLabel(gain_name, "常驻")
        return self.team_gains[gain_name]

    def create_rate(self, gain_name):
        if gain_name not in self.team_gains:
            self.team_gains[gain_name] = {}
        self.team_gains[gain_name]['rate'] = SpinWithLabel(gain_name, "覆盖(%)", maximum=100)
        return self.team_gains[gain_name]['rate']

    def create_stack(self, gain_name):
        if gain_name not in self.team_gains:
            self.team_gains[gain_name] = {}
        gain = TEAM_GAINS[gain_name]
        buff = GENERAL_BUFFS[gain.buff_id]
        self.team_gains[gain_name]['stack'] = SpinWithLabel(
            gain_name, f"层数({buff.max_stack})", maximum=buff.max_stack
        )
        return self.team_gains[gain_name]['stack']

    def create_variety(self, gain_names):
        gain_name = gain_names[0]
        if gain_name not in self.team_gains:
            self.team_gains[gain_name] = {}

        self.team_gains[gain_name]['variety'] = ComboWithLabel(
            gain_name, "种类", [""] + gain_names
        )
        return self.team_gains[gain_name]['variety']

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.team_gains = {}

        tabs = QTabWidget()
        layout.addWidget(tabs)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "七秀")

        tab_layout.addWidget(self.create_single("袖气"), 0, 0)
        tab_layout.addWidget(self.create_stack("左旋右转"), 1, 0)
        tab_layout.addWidget(self.create_rate("左旋右转"), 1, 1)
        tab_layout.addWidget(self.create_rate("泠风解怀"), 2, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "天策")

        tab_layout.addWidget(self.create_single("撼如雷"), 0, 0)
        tab_layout.addWidget(self.create_variety(["破风", "劲风"]), 1, 0)
        tab_layout.addWidget(self.create_rate("破甲"), 2, 0)
        tab_layout.addWidget(self.create_stack("号令三军"), 3, 0)
        tab_layout.addWidget(self.create_rate("号令三军"), 3, 1)
        tab_layout.addWidget(self.create_rate("激雷"), 4, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "少林")

        tab_layout.addWidget(self.create_single("立地成佛"), 0, 0)
        tab_layout.addWidget(self.create_stack("禅语"), 1, 0)
        tab_layout.addWidget(self.create_rate("禅语"), 1, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "万花")

        tab_layout.addWidget(self.create_stack("秋肃"), 0, 0)
        tab_layout.addWidget(self.create_rate("秋肃"), 0, 1)
        tab_layout.addWidget(self.create_rate("皎素"), 1, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "纯阳")

        tab_layout.addWidget(self.create_single("碎星辰"), 0, 0)
        tab_layout.addWidget(self.create_single("破苍穹"), 0, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "藏剑")

        tab_layout.addWidget(self.create_rate("百锻"), 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "五毒")

        tab_layout.addWidget(self.create_stack("仙王蛊鼎"), 0, 0)
        tab_layout.addWidget(self.create_rate("仙王蛊鼎"), 0, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "明教")

        tab_layout.addWidget(self.create_single("戒火"), 0, 0)
        tab_layout.addWidget(self.create_variety(["朝圣言", "圣浴明心"]), 1, 0)
        tab_layout.addWidget(self.create_stack("朝圣言"), 1, 1)
        tab_layout.addWidget(self.create_rate("朝圣言"), 1, 2)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "丐帮")

        tab_layout.addWidget(self.create_single("酣畅淋漓"), 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "苍云")

        tab_layout.addWidget(self.create_single("虚弱"), 0, 0)
        tab_layout.addWidget(self.create_stack("振奋"), 1, 0)
        tab_layout.addWidget(self.create_rate("振奋"), 1, 1)
        tab_layout.addWidget(self.create_rate("寒啸千军"), 2, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "长歌")

        tab_layout.addWidget(self.create_stack("庄周梦"), 0, 0)
        tab_layout.addWidget(self.create_rate("庄周梦"), 0, 1)
        tab_layout.addWidget(self.create_rate("弄梅"), 1, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "霸刀")

        tab_layout.addWidget(self.create_rate("疏狂"), 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "药宗")

        tab_layout.addWidget(self.create_rate("配伍"), 0, 0)
        tab_layout.addWidget(self.create_stack("飘黄"), 1, 0)
        tab_layout.addWidget(self.create_rate("飘黄"), 1, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "坦克")

        tab_layout.addWidget(self.create_variety(["坦克增益", "宿敌增益"]), 0, 0)

        layout.addStretch()

    def __getitem__(self, item):
        return self.team_gains[item]

    def items(self):
        return self.team_gains.items()

    def set_default(self):
        if not self.team_gains["袖气"].radio_button.isChecked():
            self.team_gains["袖气"].radio_button.click()
        self.team_gains["左旋右转"]["stack"].spin_box.setValue(100)
        self.team_gains["左旋右转"]["rate"].spin_box.setValue(100)

        if not self.team_gains["撼如雷"].radio_button.isChecked():
            self.team_gains["撼如雷"].radio_button.click()
        self.team_gains["破风"]["variety"].combo_box.setCurrentText("劲风")
        self.team_gains["破甲"]["rate"].spin_box.setValue(33)
        self.team_gains["号令三军"]["stack"].spin_box.setValue(100)
        self.team_gains["号令三军"]["rate"].spin_box.setValue(20)

        if not self.team_gains["立地成佛"].radio_button.isChecked():
            self.team_gains["立地成佛"].radio_button.click()
        self.team_gains["禅语"]["stack"].spin_box.setValue(100)
        self.team_gains["禅语"]["rate"].spin_box.setValue(100)

        self.team_gains["秋肃"]["stack"].spin_box.setValue(100)
        self.team_gains["秋肃"]["rate"].spin_box.setValue(100)
        self.team_gains["皎素"]["rate"].spin_box.setValue(14)

        self.team_gains["仙王蛊鼎"]["stack"].spin_box.setValue(100)
        self.team_gains["仙王蛊鼎"]["rate"].spin_box.setValue(100)

        if not self.team_gains["戒火"].radio_button.isChecked():
            self.team_gains["戒火"].radio_button.click()
        self.team_gains["朝圣"]["variety"].combo_box.setCurrentText("圣浴明心")
        self.team_gains["朝圣"]["stack"].spin_box.setValue(100)
        self.team_gains["朝圣"]["rate"].spin_box.setValue(7)

        if not self.team_gains["虚弱"].radio_button.isChecked():
            self.team_gains["虚弱"].radio_button.click()
        self.team_gains["振奋"]["stack"].spin_box.setValue(100)
        self.team_gains["振奋"]["rate"].spin_box.setValue(100)
        self.team_gains["寒啸千军"]["rate"].spin_box.setValue(50)

        self.team_gains["庄周梦"]["stack"].spin_box.setValue(100)
        self.team_gains["庄周梦"]["rate"].spin_box.setValue(100)

        self.team_gains["配伍"]["rate"].spin_box.setValue(100)
        self.team_gains["飘黄"]["stack"].spin_box.setValue(100)
        self.team_gains["飘黄"]["rate"].spin_box.setValue(100)

    def clear_bonuses(self):
        for bonus in self.team_gains.values():
            if isinstance(bonus, RadioWithLabel):
                if bonus.radio_button.isChecked():
                    bonus.radio_button.click()
            else:
                for sub in bonus.values():
                    if isinstance(sub, ComboWithLabel):
                        sub.combo_box.setCurrentText("")
                    elif isinstance(sub, SpinWithLabel):
                        sub.spin_box.setValue(0)


class BonusesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)
        self.activation = RadioWithLabel("启用增益", tag=True)
        top_layout.addWidget(self.activation)
        self.select_bonus = ComboWithLabel("配置增益", items=["", "开荒"])
        top_layout.addWidget(self.select_bonus)
        self.real_formulation = RadioWithLabel("开启真实增益模拟(仅包括存在覆盖率的角色属性,不包含目标和常驻属性)")
        top_layout.addWidget(self.real_formulation)
        self.tab = QTabWidget()
        layout.addWidget(self.tab)
        self.formation = FormationWidget()
        self.tab.addTab(self.formation, "阵法")
        self.team_gains = TeamGainsWidget()
        self.tab.addTab(self.team_gains, "团队增益")

        layout.addStretch()
