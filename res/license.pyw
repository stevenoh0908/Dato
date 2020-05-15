# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'license.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_license(object):
    def setupUi(self, LicenseWindow):
        LicenseWindow.setObjectName("LicenseWindow")
        LicenseWindow.resize(350, 250)
        LicenseWindow.setMinimumSize(QtCore.QSize(350, 250))
        LicenseWindow.setMaximumSize(QtCore.QSize(350, 250))
        LicenseWindow.setBaseSize(QtCore.QSize(350, 250))
        LicenseWindow.setWindowIcon(QtGui.QIcon('./img/logo.png'))
        self.verticalLayout = QtWidgets.QVBoxLayout(LicenseWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(LicenseWindow)
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

        self.retranslateUi(LicenseWindow)
        QtCore.QMetaObject.connectSlotsByName(LicenseWindow)

    def retranslateUi(self, LicenseWindow):
        _translate = QtCore.QCoreApplication.translate
        LicenseWindow.setWindowTitle(_translate("LicenseWindow", "Dato - License"))
        self.label.setText(_translate("LicenseWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">License</span></p><p align=\"center\">Dato, The Data Analysis Tools for GSHS Earth Science Team was Developed by <a href=\"https://github.com/stevenoh0908\"><span style=\" text-decoration: underline; color:#0000ff;\">Stephen Oh</span></a>, Published Under GPL v3.0 License.</p><p align=\"center\">For troubleshooting, please contact <a href=\"mailto:stevenoh0908@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">stevenoh0908@gmail.com</span></a>.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LicenseWindow = QtWidgets.QWidget()
    ui = Ui_license()
    ui.setupUi(LicenseWindow)
    LicenseWindow.show()
    sys.exit(app.exec_())
