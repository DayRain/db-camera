import time
from threading import Thread

from PySide6.QtCore import Qt, QObject, Signal, QTimer
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QFileDialog

from connect import db_utils
from core.db_manager import DbContainer
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

from core.local_constants import standard_date_format
from model.local_component import TableButton, DeleteDialog, get_icon
from model.main_window import MainWindow
from core.local_utils import time_to_str

dbContainer = DbContainer()


class DbListThread(Thread, QObject):
    update_single = Signal(list)

    def __init__(self):
        # 父类初始化
        Thread.__init__(self)
        QObject.__init__(self)

    def run(self):
        dbs = dbContainer.db_utils.get_dbs()
        self.update_single.emit(dbs)

class DataBind:
    def __init__(self, window):
        self.window = window
        self.dataBind()
        self.refreshTable(items=dbContainer.db_config.items)
        self.save_dialog = None

    def click_save_button(self, event):
        dbComboBox = self.window.dbComboBox
        if dbComboBox is not None:
            loader = QUiLoader()
            self.save_dialog = loader.load('./ui/save.ui')
            self.save_dialog.setWindowIcon(get_icon())
            self.save_dialog.dbEdit.setText(dbComboBox.currentText())
            self.save_dialog.accepted.connect(self.do_save)
            self.save_dialog.show()

    def do_save(self):
        db_name = self.save_dialog.dbEdit.text()
        show_name = self.save_dialog.nameEdit.text()
        remark = self.save_dialog.remarkEdit.text()
        self.start_task('保存中...')
        dbContainer.add_item(db_name, show_name, remark)
        self.finish_task()
        self.refreshTable(items=dbContainer.db_config.items)

    def task_progress(self, value):
        self.window.progressBar.setValue(value)
        if value == 100:
            self.finish_task()

    def start_task(self, text):
        self.window.taskLabel.setText(text)
        self.window.taskLabel.repaint()

    def finish_task(self):
        self.window.taskLabel.setText('   ')

    def dataBind(self):
        self.refresh_dbs()
        self.refreshTable(items=dbContainer.db_config.items)
        self.window.saveBtn.clicked.connect(self.click_save_button)
        self.window.searchEdit.textChanged.connect(self.search)
        self.window.settingsBtn.clicked.connect(self.click_settings_button)
        self.window.importBtn.clicked.connect(self.openFileDialog)
        self.window.taskLabel.setText('   ')

    def refresh_dbs(self):
        self.window.dbComboBox.clear()
        db_thread = DbListThread()
        db_thread.update_single.connect(self.window.dbComboBox.addItems)
        db_thread.start()

    def search(self, event):
        keyword = self.window.searchEdit.text()
        if keyword is None or keyword.isspace():
            self.refreshTable(dbContainer.db_config.items)
        else:
            items = []
            for item in dbContainer.db_config.items:
                if keyword in item.db_name or keyword in item.show_name or keyword in item.remark:
                    items.append(item)
            self.refreshTable(items)

    def click_settings_button(self):
        print('clicked')
        loader = QUiLoader()
        self.settings_dialog = loader.load('./ui/settings.ui')
        self.settings_dialog.setWindowIcon(get_icon())
        config = dbContainer.db_config
        self.settings_dialog.testBtn.clicked.connect(self.test_connection)
        self.settings_dialog.iPEdit.setText(config.ip)
        self.settings_dialog.usernameEdit.setText(config.username)
        self.settings_dialog.passwordEdit.setText(config.password)
        if self.settings_dialog.exec():
            ip = self.settings_dialog.iPEdit.text()
            username = self.settings_dialog.usernameEdit.text()
            password = self.settings_dialog.passwordEdit.text()
            config.ip = ip
            config.username = username
            config.password = password
            dbContainer.save_config()
            dbContainer.refresh()
            self.refresh_dbs()

            print("S")
        else:
            print("E")
        pass

    def openFileDialog(self):
        filenames = QFileDialog.getOpenFileNames(self.window, 'Open File')
        self.start_task('导入中...')
        for filename in filenames[0]:
            with open(filename, encoding='utf-8', )as fp:
                sql = fp.read()
                if sql is not None and not sql.isspace():
                    dbContainer.import_item(sql)
                    self.refreshTable(dbContainer.db_config.items)
        self.finish_task()

    def test_connection(self):
        ip = self.settings_dialog.iPEdit.text()
        username = self.settings_dialog.usernameEdit.text()
        password = self.settings_dialog.passwordEdit.text()
        connected = db_utils.connection_test(ip, username, password)
        if connected:
            label = '连接成功!'
        else:
            label = '连接失败!'
        self.settings_dialog.testLabel.setText(label)

    def wrap_item(self, item):
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        return item

    def refreshTable(self, items):
        table = self.window.dbTable
        table.verticalHeader().setHidden(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        if items is None or len(items) == 0:
            table.setRowCount(0)
            table.show()
            return
        row = 0
        table.setRowCount(len(items))
        table.setColumnCount(6)
        table.setItem(1, 1, QTableWidgetItem('a'))
        for item in items:
            table.setItem(row, 0, self.wrap_item(QTableWidgetItem(str(row + 1))))
            table.setItem(row, 1, self.wrap_item(QTableWidgetItem(str(item.db_name))))
            table.setItem(row, 2, self.wrap_item(QTableWidgetItem(str(item.show_name))))
            table.setItem(row, 3, self.wrap_item(QTableWidgetItem(str(item.remark))))
            table.setItem(row, 4, self.wrap_item(QTableWidgetItem(time_to_str(item.create_time, standard_date_format))))
            widget = QtWidgets.QWidget()
            widget.setFixedWidth(200)
            delete_button = TableButton('删除', item.id, dbContainer, self)
            delete_button.setFixedWidth(60)
            export_button = TableButton('导出', item.id, dbContainer, self)
            export_button.setFixedWidth(60)
            do_button = TableButton('执行', item.id, dbContainer, self)
            do_button.setFixedWidth(60)
            layout = QtWidgets.QHBoxLayout()
            layout.addWidget(delete_button)
            layout.addWidget(export_button)
            layout.addWidget(do_button)
            layout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(layout)
            table.setCellWidget(row, 5, widget)
            row = row + 1
        table.show()


def show_window():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowIcon(get_icon())
    bind = DataBind(window)
    window.show()
    app.exec()
