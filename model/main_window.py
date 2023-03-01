import sys

from PySide6 import QtWidgets

from core.log_utils import get_log
from model.ui_main import Ui_MainWindow
import traceback


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.old_hook = sys.excepthook
        sys.excepthook = self.catch_exceptions

    def catch_exceptions(self, ty, value, tb):
        """
            捕获异常，并弹窗显示
        :param ty: 异常的类型
        :param value: 异常的对象
        :param traceback: 异常的traceback
        """
        traceback_format = traceback.format_exception(ty, value, tb)
        traceback_string = "".join(traceback_format)
        get_log().error(traceback_string)
        QtWidgets.QMessageBox.critical(None, "An exception was raised", "{}".format(traceback_string))
        self.old_hook(ty, value, tb)
