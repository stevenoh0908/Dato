# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lisence.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LisenceWindow(object):
    def setupUi(self, LisenceWindow):
        LisenceWindow.setObjectName("LisenceWindow")
        LisenceWindow.resize(350, 250)
        LisenceWindow.setMinimumSize(QtCore.QSize(350, 250))
        LisenceWindow.setMaximumSize(QtCore.QSize(350, 250))
        LisenceWindow.setBaseSize(QtCore.QSize(350, 250))
        self.verticalLayout = QtWidgets.QVBoxLayout(LisenceWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(LisenceWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setOpenExternalLinks(True)
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(LisenceWindow)
        QtCore.QMetaObject.connectSlotsByName(LisenceWindow)

    def retranslateUi(self, LisenceWindow):
        _translate = QtCore.QCoreApplication.translate
        LisenceWindow.setWindowTitle(_translate("LisenceWindow", "Dato - Lisence"))
        self.label.setText(_translate("LisenceWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Lisence</span></p><p align=\"center\">Dato, The Data Analysis Tools for GSHS Earth Science Team was Developed by <a href=\"https://github.com/stevenoh0908\"><span style=\" text-decoration: underline; color:#0000ff;\">Stephen Oh</span></a>, Published Under GPL v3.0 Lisence.</p><p align=\"center\">For troubleshooting, please contact <a href=\"mailto:stevenoh0908@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">stevenoh0908@gmail.com</span></a>.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LisenceWindow = QtWidgets.QWidget()
    ui = Ui_LisenceWindow()
    ui.setupUi(LisenceWindow)
    LisenceWindow.show()
    sys.exit(app.exec_())
