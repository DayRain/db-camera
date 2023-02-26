import os
import time

from PySide6 import QtGui
from PySide6.QtWidgets import QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel

DELETE_TEXT = '删除'
EXPORT_TEXT = '导出'
ACTION_TEXT = '执行'


class TableButton(QPushButton):
    def __init__(self, text, item_id, dbContainer, view):
        super().__init__()
        self.setText(text)
        self.item_id = item_id
        self.dbContainer = dbContainer
        self.view = view
        if text == DELETE_TEXT:
            self.clicked.connect(self.delete_item)

        if text == ACTION_TEXT:
            self.clicked.connect(self.do_item)

        if text == EXPORT_TEXT:
            self.clicked.connect(self.export_item)

    def delete_item(self):
        dlg = DeleteDialog(self.view, self.dbContainer, self.item_id)
        dlg.exec_()

        self.view.refreshTable(self.dbContainer.db_config.items)

    def do_item(self):
        dlg = ActionDialog(self.dbContainer, self.item_id)
        dlg.exec_()

    def export_item(self):
        item = self.dbContainer.read_item(self.item_id)
        absolute_path = os.path.join(os.getcwd(), 'sql', item.file_name)
        os.system(r"explorer /select, " + absolute_path)


class DeleteDialog(QDialog):
    def __init__(self, view, dbContainer, item_id):
        super().__init__()
        self.view = view
        self.dbContainer = dbContainer
        self.item_id = item_id
        self.setWindowTitle("删除确认")
        self.setWindowIcon(get_icon())
        item = dbContainer.read_item(item_id)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("是否确认删除 '" + item.show_name + "' ?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept(self):
        self.dbContainer.delete_item(self.item_id)
        self.close()


class ActionDialog(QDialog):
    def __init__(self, dbContainer, item_id):
        super().__init__()
        self.dbContainer = dbContainer
        self.item_id = item_id
        self.setWindowTitle("恢复快照")
        self.setWindowIcon(get_icon())
        item = dbContainer.read_item(item_id)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("是否执行 '" + item.show_name + "' ?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept(self):
        self.dbContainer.do_item(self.item_id)
        self.close()


def get_icon():
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./ui/panda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon
