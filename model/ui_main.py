# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 601)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 781, 551))
        self.layoutWidget.setMaximumSize(QSize(16777215, 551))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dbComboBox = QComboBox(self.layoutWidget)
        self.dbComboBox.setObjectName(u"dbComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbComboBox.sizePolicy().hasHeightForWidth())
        self.dbComboBox.setSizePolicy(sizePolicy)
        self.dbComboBox.setMinimumSize(QSize(0, 30))
        self.dbComboBox.setMaximumSize(QSize(16777215, 30))
        self.dbComboBox.setEditable(True)

        self.horizontalLayout.addWidget(self.dbComboBox)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.saveBtn = QPushButton(self.layoutWidget)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy1)
        self.saveBtn.setMinimumSize(QSize(0, 30))
        self.saveBtn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.saveBtn)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.taskLabel = QLabel(self.layoutWidget)
        self.taskLabel.setObjectName(u"taskLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(80)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.taskLabel.sizePolicy().hasHeightForWidth())
        self.taskLabel.setSizePolicy(sizePolicy2)
        self.taskLabel.setMinimumSize(QSize(80, 0))
        self.taskLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.taskLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.settingsBtn = QPushButton(self.layoutWidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        sizePolicy1.setHeightForWidth(self.settingsBtn.sizePolicy().hasHeightForWidth())
        self.settingsBtn.setSizePolicy(sizePolicy1)
        self.settingsBtn.setMinimumSize(QSize(0, 30))
        self.settingsBtn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.settingsBtn)

        self.importBtn = QPushButton(self.layoutWidget)
        self.importBtn.setObjectName(u"importBtn")
        sizePolicy1.setHeightForWidth(self.importBtn.sizePolicy().hasHeightForWidth())
        self.importBtn.setSizePolicy(sizePolicy1)
        self.importBtn.setMinimumSize(QSize(0, 30))
        self.importBtn.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.importBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.searchEdit = QLineEdit(self.layoutWidget)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setMinimumSize(QSize(0, 35))
        self.searchEdit.setMaximumSize(QSize(16777215, 35))
        self.searchEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.searchEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.dbTable = QTableWidget(self.layoutWidget)
        if (self.dbTable.columnCount() < 6):
            self.dbTable.setColumnCount(6)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.dbTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dbTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dbTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dbTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dbTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dbTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.dbTable.setObjectName(u"dbTable")
        self.dbTable.setMinimumSize(QSize(0, 0))
        self.dbTable.setMaximumSize(QSize(16777215, 443))

        self.verticalLayout.addWidget(self.dbTable)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DB Camera", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.taskLabel.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u76d1\u63a7", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.importBtn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.searchEdit.setText("")
        ___qtablewidgetitem = self.dbTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.dbTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93", None));
        ___qtablewidgetitem2 = self.dbTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem3 = self.dbTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8", None));
        ___qtablewidgetitem4 = self.dbTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem5 = self.dbTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None));
    # retranslateUi

