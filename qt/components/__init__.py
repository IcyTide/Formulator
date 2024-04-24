from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtWidgets import QAbstractItemView, QTableWidgetItem, QHeaderView, QListView
from PySide6.QtWidgets import QComboBox, QRadioButton, QLineEdit, QSpinBox, QDoubleSpinBox, QListWidget, QTableWidget


class LabelWidget(QWidget):
    def __init__(self, label, info: str = ""):
        super().__init__()
        if info:
            self.label = QLabel(f"{label} - {info}")
        else:
            self.label = QLabel(label)

    def set_label(self, label):
        self.label.setText(label)


class TableWithLabel(LabelWidget):
    def __init__(self, label, row_count: int = 0, column_count: int = 0, headers: list = None):
        super().__init__(label)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()

        if row_count:
            self.table.setRowCount(row_count)
        if column_count:
            self.table.setColumnCount(column_count)
        if headers:
            self.table.setColumnCount(len(headers))
            self.table.setHorizontalHeaderLabels(headers)
        else:
            self.table.horizontalHeader().setVisible(False)

        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)

        layout.addWidget(self.label)
        layout.addWidget(self.table)

    def set_content(self, content):
        self.table.setRowCount(len(content))

        for i, row in enumerate(content):
            for j, e in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(e))


class ListWithLabel(LabelWidget):
    def __init__(self, label, max_select: int = 4, items: list = None):
        super().__init__(label)
        layout = QVBoxLayout(self)

        self.max_select = max_select

        self.list = QListWidget()
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list.setResizeMode(QListView.ResizeMode.Adjust)

        if items:
            self.set_items(items)
        layout.addWidget(self.label)
        layout.addWidget(self.list)

    def set_items(self, items):
        self.list.clear()
        self.list.addItems(items)


class ComboWithLabel(LabelWidget):
    def __init__(self, label, info: str = "", items: list = None, index=None):
        super().__init__(label, info)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.combo_box = QComboBox()
        self.items = []
        if items:
            self.set_items(items)
        if index:
            self.combo_box.setCurrentIndex(index)

        layout.addWidget(self.label)
        layout.addWidget(self.combo_box)

        layout.addStretch()

    def set_items(self, items, keep_index=False, default_index=0):
        self.items = items
        self.combo_box.blockSignals(True)
        current_text = self.combo_box.currentText()
        self.combo_box.clear()
        self.combo_box.addItems(items)
        self.combo_box.blockSignals(False)
        if keep_index and current_text and current_text in items:
            self.combo_box.setCurrentIndex(items.index(current_text))
        else:
            self.combo_box.setCurrentIndex(default_index)


class RadioWithLabel(LabelWidget):
    def __init__(self, label, text: str = None):
        super().__init__(label)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.radio_button = QRadioButton()
        if text:
            self.radio_button.setText(text)

        layout.addWidget(self.label)
        layout.addWidget(self.radio_button)

        layout.addStretch()

    def set_text(self, text):
        self.radio_button.setText(text)


class SpinWithLabel(LabelWidget):
    def __init__(self, label, info="", minimum=None, maximum=None, value=None):
        super().__init__(label, info)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.spin_box = QSpinBox()
        if minimum:
            self.spin_box.setMinimum(minimum)

        if maximum:
            self.spin_box.setMaximum(maximum + 1)
        else:
            self.spin_box.setMaximum(10 ** 8)

        if value:
            self.spin_box.setValue(value)

        layout.addWidget(self.label)
        layout.addWidget(self.spin_box)

        layout.addStretch()

    def set_value(self, value):
        self.spin_box.setValue(value)


class DoubleSpinWithLabel(LabelWidget):
    def __init__(self, label, info="", minimum=None, maximum=None, value=None):
        super().__init__(label, info)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.spin_box = QDoubleSpinBox()
        if minimum:
            self.spin_box.setMinimum(minimum)

        if maximum:
            self.spin_box.setMaximum(maximum + 1)
        else:
            self.spin_box.setMaximum(10 ** 8)

        if value:
            self.spin_box.setValue(value)

        layout.addWidget(self.label)
        layout.addWidget(self.spin_box)

        layout.addStretch()

    def set_value(self, value):
        self.spin_box.setValue(value)

class TextWithLabel(LabelWidget):
    def __init__(self, label):
        super().__init__(label)
        layout = QVBoxLayout(self)

        self.text_browser = QLineEdit()

        layout.addWidget(self.label)
        layout.addWidget(self.text_browser)

        layout.addStretch()

    def set_text(self, text):
        self.text_browser.setText(text)


class LabelWithLabel(QWidget):
    def __init__(self, label):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(label)
        self.text = QLabel()
        # self.text_browser.textChanged.connect(self.resize_height)

        layout.addWidget(self.label)
        layout.addWidget(self.text)

        layout.addStretch()

    def set_text(self, text):
        self.text.setText(text)
