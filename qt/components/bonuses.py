from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QTabWidget

from base.buff import Buff
from general.buffs import GENERAL_BUFFS
from general.gains import GENERAL_GAINS
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
    def create_single(self, buff: Buff):
        self.team_gains[buff.buff_name] = RadioWithLabel(buff.buff_name, "常驻")
        return self.team_gains[buff.buff_name]

    def create_rate(self, buff: Buff):
        if buff.buff_name not in self.team_gains:
            self.team_gains[buff.buff_name] = {}
        self.team_gains[buff.buff_name]['rate'] = SpinWithLabel(buff.buff_name, "覆盖(%)", maximum=100)
        return self.team_gains[buff.buff_name]['rate']

    def create_stack(self, buff: Buff):
        if buff.buff_name not in self.team_gains:
            self.team_gains[buff.buff_name] = {}
        self.team_gains[buff.buff_name]['stack'] = SpinWithLabel(
            buff.buff_name, f"层数({buff.max_stack})", maximum=buff.max_stack
        )
        return self.team_gains[buff.buff_name]['stack']

    def create_variety(self, buff: Buff):
        if buff.buff_name not in self.team_gains:
            self.team_gains[buff.buff_name] = {}

        self.team_gains[buff.buff_name]['variety'] = ComboWithLabel(
            buff.buff_name, "种类", [""] + list(TEAM_GAINS[buff.buff_name].attributes)
        )
        return self.team_gains[buff.buff_name]['variety']

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.team_gains = {}

        tabs = QTabWidget()
        layout.addWidget(tabs)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "七秀")

        tab_layout.addWidget(self.create_single(GENERAL_GAINS[673]), 0, 0)
        tab_layout.addWidget(self.create_stack(GENERAL_BUFFS[20938]), 1, 0)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[20938]), 1, 1)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[23573]), 2, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "天策")

        tab_layout.addWidget(self.create_single(GENERAL_GAINS[362]), 0, 0)
        tab_layout.addWidget(self.create_variety(GENERAL_GAINS[661]), 1, 0)
        tab_layout.addWidget(self.create_rate(GENERAL_GAINS[3465]), 2, 0)
        tab_layout.addWidget(self.create_stack(GENERAL_BUFFS[23107]), 3, 0)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[23107]), 3, 1)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[6363]), 4, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "少林")

        tab_layout.addWidget(self.create_single(GENERAL_GAINS[566]), 0, 0)
        tab_layout.addWidget(self.create_stack(GENERAL_BUFFS[10208]), 1, 0)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[10208]), 1, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "万花")

        tab_layout.addWidget(self.create_single(GENERAL_GAINS[23305]), 0, 0)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[24350]), 1, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "纯阳")

        tab_layout.addWidget(self.create_single(GENERAL_GAINS[378]), 0, 0)
        tab_layout.addWidget(self.create_single(GENERAL_GAINS[375]), 0, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "藏剑")

        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[21236]), 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "五毒")

        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[24742]), 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "明教")

        tab_layout.addWidget(self.create_single(GENERAL_GAINS[4058]), 0, 0)
        tab_layout.addWidget(self.create_variety(GENERAL_BUFFS[4246]), 1, 0)
        tab_layout.addWidget(self.create_stack(GENERAL_BUFFS[4246]), 1, 1)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[4246]), 1, 2)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "丐帮")

        tab_layout.addWidget(self.create_single(GENERAL_GAINS[7180]), 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "苍云")

        tab_layout.addWidget(self.create_single(GENERAL_GAINS[8248]), 0, 0)
        tab_layout.addWidget(self.create_stack(GENERAL_BUFFS[8504]), 1, 0)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[8504]), 1, 1)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[10031]), 2, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "长歌")

        tab_layout.addWidget(self.create_stack(GENERAL_BUFFS[23543]), 0, 0)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[23543]), 0, 1)
        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[16911]), 1, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "霸刀")

        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[11456]), 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "药宗")

        tab_layout.addWidget(self.create_rate(GENERAL_BUFFS[20877]), 0, 0)

        layout.addStretch()

    def __getitem__(self, item):
        return self.team_gains[item]

    def items(self):
        return self.team_gains.items()

    def set_default(self):
        self.team_gains["袖气"].radio_button.click()
        self.team_gains["左旋右转"]["stack"].spin_box.setValue(120)
        self.team_gains["左旋右转"]["rate"].spin_box.setValue(100)

        self.team_gains["撼如雷"].radio_button.click()
        self.team_gains["破风"]["variety"].combo_box.setCurrentText("劲风")
        self.team_gains["破甲"]["rate"].spin_box.setValue(33)
        self.team_gains["号令三军"]["stack"].spin_box.setValue(48)
        self.team_gains["号令三军"]["rate"].spin_box.setValue(20)

        self.team_gains["立地成佛"].radio_button.click()
        self.team_gains["弘法"]["stack"].spin_box.setValue(36)
        self.team_gains["弘法"]["rate"].spin_box.setValue(50)

        self.team_gains["秋肃"].radio_button.click()
        self.team_gains["皎素"]["rate"].spin_box.setValue(14)

        self.team_gains["仙王蛊鼎"]["rate"].spin_box.setValue(21)

        self.team_gains["戒火"].radio_button.click()
        self.team_gains["朝圣"]["variety"].combo_box.setCurrentText("圣浴明心")
        self.team_gains["朝圣"]["stack"].spin_box.setValue(24)
        self.team_gains["朝圣"]["rate"].spin_box.setValue(7)

        self.team_gains["虚弱"].radio_button.click()
        self.team_gains["振奋"]["stack"].spin_box.setValue(87)
        self.team_gains["振奋"]["rate"].spin_box.setValue(100)
        self.team_gains["寒啸千军"]["rate"].spin_box.setValue(50)

        self.team_gains["庄周梦"]["stack"].spin_box.setValue(120)
        self.team_gains["庄周梦"]["rate"].spin_box.setValue(75)

        self.team_gains["配伍"]["rate"].spin_box.setValue(100)


class BonusesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)
        self.activation = RadioWithLabel("启用增益")
        top_layout.addWidget(self.activation)
        self.real_formulation = RadioWithLabel("开启真实增益模拟(仅包括存在覆盖率的角色属性,不包含目标和常驻属性)")
        top_layout.addWidget(self.real_formulation)
        self.tab = QTabWidget()
        layout.addWidget(self.tab)
        self.formation = FormationWidget()
        self.tab.addTab(self.formation, "阵法")
        self.team_gains = TeamGainsWidget()
        self.tab.addTab(self.team_gains, "团队增益")

        layout.addStretch()
