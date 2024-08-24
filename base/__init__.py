# import sys
# from PySide6.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
#     QComboBox, QPushButton, QListWidget
# )
#
# class BuffManager(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Buff Manager")
#
#         # 初始化布局
#         main_layout = QVBoxLayout()
#         selection_layout = QHBoxLayout()
#         status_layout = QHBoxLayout()
#
#         # Buff ID 选择框
#         self.buff_id_label = QLabel("Buff ID:")
#         self.buff_id_combo = QComboBox()
#         self.buff_id_combo.addItems(["Buff1", "Buff2", "Buff3"])  # 示例数据
#         self.buff_id_combo.currentIndexChanged.connect(self.update_buff_level_options)
#
#         # Buff Level 选择框
#         self.buff_level_label = QLabel("Buff Level:")
#         self.buff_level_combo = QComboBox()
#
#         # Buff Stack 选择框
#         self.buff_stack_label = QLabel("Buff Stack:")
#         self.buff_stack_combo = QComboBox()
#
#         # Buff Name 显示标签
#         self.buff_name_label = QLabel("Buff Name:")
#         self.buff_name_display = QLabel("N/A")
#
#         # 将选择控件加入布局
#         selection_layout.addWidget(self.buff_id_label)
#         selection_layout.addWidget(self.buff_id_combo)
#         selection_layout.addWidget(self.buff_level_label)
#         selection_layout.addWidget(self.buff_level_combo)
#         selection_layout.addWidget(self.buff_stack_label)
#         selection_layout.addWidget(self.buff_stack_combo)
#         selection_layout.addWidget(self.buff_name_label)
#         selection_layout.addWidget(self.buff_name_display)
#
#         # CurrentStatus 和 SnapshotStatus 列表
#         self.current_status_label = QLabel("CurrentStatus:")
#         self.current_status_list = QListWidget()
#         self.current_status_list.itemClicked.connect(self.load_selected_status)
#
#         self.snapshot_status_label = QLabel("SnapshotStatus:")
#         self.snapshot_status_list = QListWidget()
#         self.snapshot_status_list.itemClicked.connect(self.load_selected_status)
#
#         # 添加、移除和修改按钮
#         self.add_to_current_button = QPushButton("Add to CurrentStatus")
#         self.add_to_snapshot_button = QPushButton("Add to SnapshotStatus")
#         self.remove_from_current_button = QPushButton("Remove from CurrentStatus")
#         self.remove_from_snapshot_button = QPushButton("Remove from SnapshotStatus")
#
#         self.add_to_current_button.clicked.connect(self.add_to_current_status)
#         self.add_to_snapshot_button.clicked.connect(self.add_to_snapshot_status)
#         self.remove_from_current_button.clicked.connect(self.remove_from_current_status)
#         self.remove_from_snapshot_button.clicked.connect(self.remove_from_snapshot_status)
#
#         # 将按钮和列表加入布局
#         status_layout.addWidget(self.current_status_label)
#         status_layout.addWidget(self.current_status_list)
#         status_layout.addWidget(self.snapshot_status_label)
#         status_layout.addWidget(self.snapshot_status_list)
#         status_layout.addWidget(self.add_to_current_button)
#         status_layout.addWidget(self.add_to_snapshot_button)
#         status_layout.addWidget(self.remove_from_current_button)
#         status_layout.addWidget(self.remove_from_snapshot_button)
#
#         # 将所有布局加入主布局
#         main_layout.addLayout(selection_layout)
#         main_layout.addLayout(status_layout)
#         self.setLayout(main_layout)
#
#         # 初始加载 Buff Level 和 Buff Stack 选项
#         self.update_buff_level_options()
#
#     def update_buff_level_options(self):
#         # 根据选择的 Buff ID 更新 Buff Level 选项
#         buff_id = self.buff_id_combo.currentText()
#         if buff_id == "Buff1":
#             levels = ["1", "2", "3"]
#         elif buff_id == "Buff2":
#             levels = ["1", "2"]
#         else:
#             levels = ["1"]
#         self.buff_level_combo.clear()
#         self.buff_level_combo.addItems(levels)
#         self.update_buff_stack_options()
#
#     def update_buff_stack_options(self):
#         # 根据选择的 Buff Level 更新 Buff Stack 和 Buff Name
#         level = self.buff_level_combo.currentText()
#         if level == "1":
#             stacks = ["1", "2", "3"]
#             name = "Basic Buff"
#         elif level == "2":
#             stacks = ["1", "2"]
#             name = "Intermediate Buff"
#         else:
#             stacks = ["1"]
#             name = "Advanced Buff"
#         self.buff_stack_combo.clear()
#         self.buff_stack_combo.addItems(stacks)
#         self.buff_name_display.setText(name)
#
#     def add_to_current_status(self):
#         # 将选择的 Buff 添加到 CurrentStatus
#         buff_info = f"{self.buff_id_combo.currentText()} - {self.buff_level_combo.currentText()} - {self.buff_stack_combo.currentText()}"
#         self.current_status_list.addItem(buff_info)
#
#     def add_to_snapshot_status(self):
#         # 将选择的 Buff 添加到 SnapshotStatus
#         buff_info = f"{self.buff_id_combo.currentText()} - {self.buff_level_combo.currentText()} - {self.buff_stack_combo.currentText()}"
#         self.snapshot_status_list.addItem(buff_info)
#
#     def remove_from_current_status(self):
#         # 从 CurrentStatus 移除选择的 Buff
#         selected_item = self.current_status_list.currentItem()
#         if selected_item:
#             self.current_status_list.takeItem(self.current_status_list.row(selected_item))
#
#     def remove_from_snapshot_status(self):
#         # 从 SnapshotStatus 移除选择的 Buff
#         selected_item = self.snapshot_status_list.currentItem()
#         if selected_item:
#             self.snapshot_status_list.takeItem(self.snapshot_status_list.row(selected_item))
#
#     def load_selected_status(self, item):
#         # 将点击的列表项内容载入到 Buff 选择框中
#         buff_info = item.text()
#         buff_id, buff_level, buff_stack = buff_info.split(" - ")
#
#         # 更新 Buff ID
#         self.buff_id_combo.setCurrentText(buff_id)
#
#         # 更新 Buff Level
#         self.update_buff_level_options()
#         self.buff_level_combo.setCurrentText(buff_level)
#
#         # 更新 Buff Stack
#         self.buff_stack_combo.setCurrentText(buff_stack)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = BuffManager()
#     window.show()
#     sys.exit(app.exec())
