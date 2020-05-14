# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageManager.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(3,0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLog = QtWidgets.QMenu(self.menubar)
        self.menuLog.setObjectName("menuLog")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionUserOption = QtWidgets.QAction(MainWindow)
        self.actionUserOption.setObjectName("actionUserOption")
        self.actionUserHelp = QtWidgets.QAction(MainWindow)
        self.actionUserHelp.setObjectName("actionUserHelp")
        self.actionLisense = QtWidgets.QAction(MainWindow)
        self.actionLisense.setObjectName("actionLisense")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_Log_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_Log_File.setObjectName("actionOpen_Log_File")
        self.actionLog_Options = QtWidgets.QAction(MainWindow)
        self.actionLog_Options.setObjectName("actionLog_Options")
        self.actionConfigureLog = QtWidgets.QAction(MainWindow)
        self.actionConfigureLog.setObjectName("actionConfigureLog")
        self.actionOpenLogFile = QtWidgets.QAction(MainWindow)
        self.actionOpenLogFile.setObjectName("actionOpenLogFile")
        self.actionLogOption = QtWidgets.QAction(MainWindow)
        self.actionLogOption.setObjectName("actionLogOption")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuLog.addAction(self.actionConfigureLog)
        self.menuLog.addSeparator()
        self.menuLog.addAction(self.actionOpenLogFile)
        self.menuLog.addAction(self.actionLogOption)
        self.menuOption.addAction(self.actionUserOption)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionUserHelp)
        self.menuOption.addAction(self.actionLisense)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dato - Image Manager"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLog.setTitle(_translate("MainWindow", "Log"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionOpen.setText(_translate("MainWindow", "Open Image"))
        self.actionClose.setText(_translate("MainWindow", "Close Image"))
        self.actionUserOption.setText(_translate("MainWindow", "User Option"))
        self.actionUserHelp.setText(_translate("MainWindow", "Help"))
        self.actionLisense.setText(_translate("MainWindow", "Lisence"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_Log_File.setText(_translate("MainWindow", "Open Log File"))
        self.actionLog_Options.setText(_translate("MainWindow", "Log Options"))
        self.actionConfigureLog.setText(_translate("MainWindow", "Configure Log"))
        self.actionOpenLogFile.setText(_translate("MainWindow", "Open Log File"))
        self.actionLogOption.setText(_translate("MainWindow", "Log Option"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
