# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageManager.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_imageManager(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        MainWindow.setWindowIcon(QtGui.QIcon('./img/logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeView(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
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
        self.actionUserOption = QtWidgets.QAction(MainWindow)
        self.actionUserOption.setObjectName("actionUserOption")
        self.actionUserHelp = QtWidgets.QAction(MainWindow)
        self.actionUserHelp.setObjectName("actionUserHelp")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_Log_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_Log_File.setObjectName("actionOpen_Log_File")
        self.actionConfigureLog = QtWidgets.QAction(MainWindow)
        self.actionConfigureLog.setObjectName("actionConfigureLog")
        self.actionOpenLogFile = QtWidgets.QAction(MainWindow)
        self.actionOpenLogFile.setObjectName("actionOpenLogFile")
        self.actionLogOption = QtWidgets.QAction(MainWindow)
        self.actionLogOption.setObjectName("actionLogOption")
        self.menuFile.addAction(self.actionOpen)
        self.menuLog.addAction(self.actionConfigureLog)
        self.menuLog.addSeparator()
        self.menuLog.addAction(self.actionOpenLogFile)
        self.menuLog.addAction(self.actionLogOption)
        self.menuOption.addAction(self.actionUserOption)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionUserHelp)
        self.menuOption.addAction(self.actionLicense)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())

        self.actionOpen.triggered.connect(self.actionOpenClicked)
        self.actionUserOption.triggered.connect(self.actionUserOptionClicked)
        self.actionUserHelp.triggered.connect(self.actionUserHelpClicked)
        self.actionLicense.triggered.connect(self.actionLicenseClicked)
        self.actionExit.triggered.connect(self.actionExitClicked)
        self.actionOpen_Log_File.triggered.connect(self.actionOpen_Log_FileClicked)
        self.actionConfigureLog.triggered.connect(self.actionConfigureLogClicked)
        self.actionLogOption.triggered.connect(self.actionLogOptionClicked)

        self.treeWidget.doubleClicked.connect(self.treeItemDoubleClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dato - Image Manager"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLog.setTitle(_translate("MainWindow", "Log"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionOpen.setText(_translate("MainWindow", "Open Directory"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionUserOption.setText(_translate("MainWindow", "User Option"))
        self.actionUserHelp.setText(_translate("MainWindow", "Help"))
        self.actionLicense.setText(_translate("MainWindow", "Licence"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen_Log_File.setText(_translate("MainWindow", "Open Log File"))
        self.actionConfigureLog.setText(_translate("MainWindow", "Configure Log"))
        self.actionOpenLogFile.setText(_translate("MainWindow", "Open Log File"))
        self.actionLogOption.setText(_translate("MainWindow", "Log Options"))

    def initVariables(self):
        self.directoryModel = QtWidgets.QFileSystemModel()
        self.directoryModel.setRootPath(QtCore.QDir.currentPath())
        self.treeWidget.setModel(self.directoryModel)
        self.treeWidget.setRootIndex(self.directoryModel.index(QtCore.QDir.currentPath()))
        self.treeWidget.setWindowTitle("Dircetory...")

    def treeItemDoubleClicked(self, index):
        self.filepath = index.model().filePath(index)
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(self.filepath))
        self.graphicsView.setScene(scene)
        self.graphicsView.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.graphicsView.show()
        pass

    def actionOpenClicked(self):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory(MainWindow, "Open Directory"))
        self.directoryModel.setRootPath(directory)
        self.treeWidget.setModel(self.directoryModel)
        self.treeWidget.setRootIndex(self.directoryModel.index(directory))
        pass

    def actionUserOptionClicked(self):
        pass

    def actionUserHelpClicked(self):
        pass

    def actionLicenseClicked(self):
        subprocess.Popen('pythonw license.pyw', shell=True)
        pass

    def actionExitClicked(self):
        exit()
        pass

    def actionOpen_Log_FileClicked(self):
        pass

    def actionConfigureLogClicked(self):
        pass

    def actionLogOptionClicked(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_imageManager()
    ui.setupUi(MainWindow)
    ui.initVariables()
    MainWindow.show()
    sys.exit(app.exec_())
