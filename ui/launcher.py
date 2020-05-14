# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LauncherWindow(object):
    def setupUi(self, LauncherWindow):
        LauncherWindow.setObjectName("LauncherWindow")
        LauncherWindow.resize(150, 200)
        self.centralwidget = QtWidgets.QWidget(LauncherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButtonTableManager = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButtonTableManager.setFont(font)
        self.pushButtonTableManager.setObjectName("pushButtonTableManager")
        self.verticalLayout.addWidget(self.pushButtonTableManager)
        self.pushButtonImageManager = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButtonImageManager.setFont(font)
        self.pushButtonImageManager.setObjectName("pushButtonImageManager")
        self.verticalLayout.addWidget(self.pushButtonImageManager)
        self.pushButtonExit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.verticalLayout.addWidget(self.pushButtonExit)
        LauncherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LauncherWindow)
        QtCore.QMetaObject.connectSlotsByName(LauncherWindow)

    def retranslateUi(self, LauncherWindow):
        _translate = QtCore.QCoreApplication.translate
        LauncherWindow.setWindowTitle(_translate("LauncherWindow", "Dato - Launcher"))
        self.label.setText(_translate("LauncherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600;\">Dato</span></p></body></html>"))
        self.pushButtonTableManager.setText(_translate("LauncherWindow", "Table Manager"))
        self.pushButtonImageManager.setText(_translate("LauncherWindow", "Image Manager"))
        self.pushButtonExit.setText(_translate("LauncherWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LauncherWindow = QtWidgets.QMainWindow()
    ui = Ui_LauncherWindow()
    ui.setupUi(LauncherWindow)
    LauncherWindow.show()
    sys.exit(app.exec_())
