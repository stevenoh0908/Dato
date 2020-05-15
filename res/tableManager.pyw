# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableManager.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

'''
{ Dato - tableManager.pyw }

Dato is GUI Application for analyzing complex data, which is dedicated to GSHS Earth-Science Team,
developed by Stephen Oh.

Latest Modification Date: 2020-05-14 Thur, KST
Developed by Stephen Oh, Chief Developer of Trendous Development Alliance & Studio.Chem
Email Address: stevenoh0908@gmail.com

> Warning
This Code uses PyQt and ba2cc for execution, please make sure that you've installed them already,
'''


from PyQt5 import QtCore, QtGui, QtWidgets
from ba2cc.ba2cc import BAManager, FileManager, DataManager, ExtremeManager
import subprocess, webbrowser


class Ui_tableManager(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        MainWindow.setWindowIcon(QtGui.QIcon('./img/logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAnalyze = QtWidgets.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        self.menuCalculateBorder = QtWidgets.QMenu(self.menuAnalyze)
        self.menuCalculateBorder.setObjectName("menuCalculateBorder")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionAddRow = QtWidgets.QAction(MainWindow)
        self.actionAddRow.setObjectName("actionAddRow")
        self.actionDeleteRows = QtWidgets.QAction(MainWindow)
        self.actionDeleteRows.setObjectName("actionDeleteRows")
        self.actionDeleteAll = QtWidgets.QAction(MainWindow)
        self.actionDeleteAll.setObjectName("actionDeleteAll")
        self.actionDisplayDataDistributionChart = QtWidgets.QAction(MainWindow)
        self.actionDisplayDataDistributionChart.setObjectName("actionDisplayDataDistributionChart")
        self.actionDisplayBorderDistributionChart = QtWidgets.QAction(MainWindow)
        self.actionDisplayBorderDistributionChart.setObjectName("actionDisplayBorderDistributionChart")
        self.actionClearExtremes = QtWidgets.QAction(MainWindow)
        self.actionClearExtremes.setObjectName("actionClearExtremes")
        self.actionEntropyBorderAlgorithm = QtWidgets.QAction(MainWindow)
        self.actionEntropyBorderAlgorithm.setObjectName("actionEntropyBorderAlgorithm")
        self.actionSignedBorderAlgorithm = QtWidgets.QAction(MainWindow)
        self.actionSignedBorderAlgorithm.setObjectName("actionSignedBorderAlgorithm")
        self.actionUnsignedBorderAlgorithm = QtWidgets.QAction(MainWindow)
        self.actionUnsignedBorderAlgorithm.setObjectName("actionUnsignedBorderAlgorithm")
        self.actionSignedMeanBorderAlgorithm = QtWidgets.QAction(MainWindow)
        self.actionSignedMeanBorderAlgorithm.setObjectName("actionSignedMeanBorderAlgorithm")
        self.actionUnsignedMeanBorderAlgorithm = QtWidgets.QAction(MainWindow)
        self.actionUnsignedMeanBorderAlgorithm.setObjectName("actionUnsignedMeanBorderAlgorithm")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.menuUser_Option = QtWidgets.QMenu(self.menuOption)
        self.menuUser_Option.setObjectName("actionUser_Option")
        self.actionCategory1 = QtWidgets.QAction(MainWindow)
        self.actionCategory1.setObjectName("actionCategory1")
        self.actionCategory2 = QtWidgets.QAction(MainWindow)
        self.actionCategory2 = QtWidgets.QAction(MainWindow)
        self.actionStep = QtWidgets.QAction(MainWindow)
        self.actionStep.setObjectName("actionStep")
        self.actionDisplayMode = QtWidgets.QAction(MainWindow)
        self.actionDisplayMode.setObjectName("actionDisplayMode")
        self.actionOffset = QtWidgets.QAction(MainWindow)
        self.actionOffset.setObjectName("actionOffset")
        self.actionUserHelp = QtWidgets.QAction(MainWindow)
        self.actionUserHelp.setObjectName("actionUserHelp")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionAddRow)
        self.menuEdit.addAction(self.actionDeleteRows)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDeleteAll)
        self.menuCalculateBorder.addAction(self.actionEntropyBorderAlgorithm)
        self.menuCalculateBorder.addSeparator()
        self.menuCalculateBorder.addAction(self.actionSignedBorderAlgorithm)
        self.menuCalculateBorder.addAction(self.actionUnsignedBorderAlgorithm)
        self.menuCalculateBorder.addAction(self.actionSignedMeanBorderAlgorithm)
        self.menuCalculateBorder.addAction(self.actionUnsignedMeanBorderAlgorithm)
        self.menuAnalyze.addAction(self.actionClearExtremes)
        self.menuAnalyze.addSeparator()
        self.menuAnalyze.addAction(self.actionDisplayDataDistributionChart)
        self.menuAnalyze.addAction(self.actionDisplayBorderDistributionChart)
        self.menuAnalyze.addSeparator()
        self.menuAnalyze.addAction(self.menuCalculateBorder.menuAction())
        self.menuUser_Option.addAction(self.actionCategory1)
        self.menuUser_Option.addAction(self.actionCategory2)
        self.menuUser_Option.addSeparator()
        self.menuUser_Option.addAction(self.actionStep)
        self.menuUser_Option.addAction(self.actionDisplayMode)
        self.menuUser_Option.addAction(self.actionOffset)
        self.menuOption.addAction(self.menuUser_Option.menuAction())
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionUserHelp)
        self.menuOption.addAction(self.actionLicense)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())

        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)

        self.actionNew.triggered.connect(self.actionNewClicked)
        self.actionOpen.triggered.connect(self.actionOpenClicked)
        self.actionSave.triggered.connect(self.actionSaveClicked)
        self.actionSave_As.triggered.connect(self.actionSave_AsClicked)
        self.actionAddRow.triggered.connect(self.actionAddRowClicked)
        self.actionDeleteRows.triggered.connect(self.actionDeleteRowsClicked)
        self.actionDeleteAll.triggered.connect(self.actionDeleteAllClicked)
        self.actionClearExtremes.triggered.connect(self.actionClearExtremesClicked)
        self.actionDisplayDataDistributionChart.triggered.connect(self.actionDisplayDataDistributionChartClicked)
        self.actionDisplayBorderDistributionChart.triggered.connect(self.actionDisplayBorderDistributionChartClicked)
        self.actionEntropyBorderAlgorithm.triggered.connect(self.actionEntropyBorderAlgorithmClicked)
        self.actionSignedBorderAlgorithm.triggered.connect(self.actionSignedBorderAlgorithmClicked)
        self.actionUnsignedBorderAlgorithm.triggered.connect(self.actionUnsignedBorderAlgorithmClicked)
        self.actionSignedMeanBorderAlgorithm.triggered.connect(self.actionSignedMeanBorderAlgorithmClicked)
        self.actionUnsignedMeanBorderAlgorithm.triggered.connect(self.actionUnsignedMeanBorderAlgorithmClicked)
        self.actionLicense.triggered.connect(self.actionLicenseClicked)
        self.actionCategory1.triggered.connect(self.actionCategory1Clicked)
        self.actionCategory2.triggered.connect(self.actionCategory2Clicked)
        self.actionStep.triggered.connect(self.actionStepClicked)
        self.actionDisplayMode.triggered.connect(self.actionDisplayModeClicked)
        self.actionOffset.triggered.connect(self.actionOffsetClicked)
        self.actionUserHelp.triggered.connect(self.actionUserHelpClicked)
        self.actionExit.triggered.connect(self.actionExitClicked)

        self.tableWidget.cellChanged.connect(self.tableWidgetcellChanged)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dato - Table Manager"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.menuCalculateBorder.setTitle(_translate("MainWindow", "Calculate Border"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionAddRow.setText(_translate("MainWindow", "Add Row"))
        self.actionAddRow.setShortcut(_translate("MainWindow", "Shift+Return"))
        self.actionDeleteRows.setText(_translate("MainWindow", "Delete Selected Row(s)"))
        self.actionDeleteRows.setShortcut(_translate("MainWindow", "Shift+Delete"))
        self.actionDeleteAll.setText(_translate("MainWindow", "Delete All"))
        self.actionDeleteAll.setShortcut(_translate("MainWindow", "Ctrl+Shift+Delete"))
        self.actionClearExtremes.setText(_translate("MainWindow", "Clear Extremes"))
        self.actionDisplayDataDistributionChart.setText(_translate("MainWindow", "Display Data Distribution Chart"))
        self.actionDisplayBorderDistributionChart.setText(_translate("MainWindow", "Display Border Distribution Chart"))
        self.actionEntropyBorderAlgorithm.setText(_translate("MainWindow", "Entropy Border Algorithm"))
        self.actionSignedBorderAlgorithm.setText(_translate("MainWindow", "Signed Border Algorithm"))
        self.actionUnsignedBorderAlgorithm.setText(_translate("MainWindow", "Unsigned Border Algorithm"))
        self.actionSignedMeanBorderAlgorithm.setText(_translate("MainWindow", "Signed Mean Border Algorithm"))
        self.actionUnsignedMeanBorderAlgorithm.setText(_translate("MainWindow", "Unsigned Mean Border Algorithm"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.menuUser_Option.setTitle(_translate("MainWindow", "Option"))
        self.actionCategory1.setText(_translate("MainWindow", "Category 1 Name"))
        self.actionCategory2.setText(_translate("MainWindow", "Category 2 Name"))
        self.actionStep.setText(_translate("MainWindow", "Border Step"))
        self.actionDisplayMode.setText(_translate("MainWindow", "Chart Display Mode"))
        self.actionOffset.setText(_translate("MainWindow", "Extreme Offset"))
        self.actionUserHelp.setText(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def setupVariables(self):
        self.EDITED = False
        self.SAVED = False
        self.BORDER_CALCULATED = False
        self.CLEARED_EXTREMES = False
        self.filename = None
        self.catname1 = 'Category 1'
        self.catname2 = 'Category 2'
        self.step = 0.1
        self.offset = 10
        self.border = None
        self.option = BAManager.OPTION_UNLAYERED
        self.updateStatusBar()
        self.updateTableLabel()

    def updateStatusBar(self):
        self.statusbar.showMessage(
            str(self.filename) + ' | ' +
            ('Edited' if self.EDITED else 'UnEdited') + ' | ' +
            ('Saved' if self.SAVED else 'UnSaved') + ' | ' +
            ('Cleared Extremes' if self.CLEARED_EXTREMES else 'Uncleared Extremes') + ' | ' +
            'Step: ' + str(self.step) + ' | ' +
            'Offset : ' + str(self.offset) + ' | ' +
            ('Unlayered Display' if self.option == BAManager.OPTION_UNLAYERED else 'Layered Display'))
        pass

    def updateTableLabel(self):
        self.tableWidget.setHorizontalHeaderLabels([self.catname1, self.catname2])
        pass        
    
    def tableWidgetcellChanged(self):
        self.EDITED = True
        self.SAVED = False
        self.updateStatusBar()
        pass

    def actionNewClicked(self):
        if self.EDITED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, 'The table has been modified.', "Do you want to discard it and make new one anyways?", (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No), QtWidgets.QMessageBox.No)
            if not resp == QtWidgets.QMessageBox.Yes:
                return
            pass
        self.filename = None
        self.tableWidget.clear()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.EDITED = False
        self.SAVED = False
        self.CLEARED_EXTREMES = False
        self.updateStatusBar()
        self.updateTableLabel()
        pass

    def actionOpenClicked(self):
        if self.EDITED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, 'The table has been modified.', "Do you want to discard it and open new one anyways?", (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No), QtWidgets.QMessageBox.No)
            if not resp == QtWidgets.QMessageBox.Yes:
                return
            pass
        self.filename = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File', './', 'CSV Files(*.csv)')[0]
        if self.filename:
            self.fileManager = FileManager(self.filename)
            self.cat1, self.cat2 = self.fileManager.loadData()
            if self.cat1 == None and self.cat2 == None:
                resp = QtWidgets.QMessageBox.warning(MainWindow, "File Reading Error!", "There was error with opening a file. Please check your target file it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                return
            self.tableWidget.setRowCount(len(self.cat1) if len(self.cat1) >= len(self.cat2) else len(self.cat2))
            for row in range(0, (len(self.cat1) if len(self.cat1) >= len(self.cat2) else len(self.cat2)), 1):
                self.tableWidget.setItem(row,0, QtWidgets.QTableWidgetItem(str(self.cat1[row]) if not len(str(self.cat1[row])) == 0 else ''))
                self.tableWidget.setItem(row,1, QtWidgets.QTableWidgetItem(str(self.cat2[row]) if not len(str(self.cat2[row])) == 0 else ''))
                pass
            self.EDITED = True
            self.SAVED = True
            self.CLEARED_EXTREMES = False
            self.updateStatusBar()
            pass
        pass

    def actionSaveClicked(self):
        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save File', './', 'CSV Files(*.csv)')[0]
            pass
        self.fileManager = FileManager(self.filename)
        cat1 = []
        cat2 = []
        for row in range(0, self.tableWidget.rowCount(), 1):
            if self.tableWidget.item(row, 0) == None and self.tableWidget.item(row, 1) == None:
                resp = QtWidgets.QMessageBox.warning(MainWindow, "File Saving Error!", "There was error with saving a file. Please check your table it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                return
            if self.tableWidget.item(row, 0) == None and row+1 < self.tableWidget.rowCount() and not self.tableWidget.item(row+1, 0) == None:
                resp = QtWidgets.QMessageBox.warning(MainWindow, "File Saving Error!", "There was error with saving a file. Please check your table it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                return
            if self.tableWidget.item(row, 1) == None and row+1< self.tableWidget.rowCount() and not self.tableWidget.item(row+1, 1) == None:
                resp = QtWidgets.QMessageBox.warning(MainWindow, "File Saving Error!", "There was error with saving a file. Please check your table it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                return
            if not self.tableWidget.item(row, 0) == None and not self.tableWidget.item(row, 1) == None:
                if self.tableWidget.item(row, 0).text() == '' and self.tableWidget.item(row, 1).text() == '':
                    resp = QtWidgets.QMessageBox.warning(MainWindow, "File Saving Error!", "There was error with saving a file. Please check your table it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                    return
                pass
            if not self.tableWidget.item(row, 0) == None and not self.tableWidget.item(row+1, 0) == None:
                if self.tableWidget.item(row, 0).text() == '' and row+1 < self.tableWidget.rowCount() and not self.tableWidget.item(row+1, 0).text() == '':
                    resp = QtWidgets.QMessageBox.warning(MainWindow, "File Saving Error!", "There was error with saving a file. Please check your table it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                    return
                pass
            if not self.tableWidget.item(row, 1) == None and not self.tableWidget.item(row+1, 1) == None:
                if self.tableWidget.item(row, 1).text() == '' and row+1< self.tableWidget.rowCount() and not self.tableWidget.item(row+1, 1).text() == '':
                    resp = QtWidgets.QMessageBox.warning(MainWindow, "File Saving Error!", "There was error with saving a file. Please check your table it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                    return
                pass
            cat1.append(self.tableWidget.item(row, 0).text() if not self.tableWidget.item(row, 0) == None else '')
            cat2.append(self.tableWidget.item(row, 1).text() if not self.tableWidget.item(row, 1) == None else '')
            pass
        self.fileManager.writeData(cat1, cat2)
        self.SAVED = True
        self.EDITED = False
        self.CLEARED_EXTREMES = False
        self.updateStatusBar()
        pass

    def actionSave_AsClicked(self):
        self.filename = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save File As', './', 'CSV Files(*.csv)')[0]
        self.fileManager = FileManager(self.filename)
        cat1 = []
        cat2 = []
        for row in range(0, self.tableWidget.rowCount(), 1):
            if self.tableWidget.item(row, 0) == None and self.tableWidget.item(row, 1) == None:
                resp = QtWidgets.QMessageBox.warning(MainWindow, "File Saving Error!", "There was error with saving a file. Please check your table it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                return
            if self.tableWidget.item(row, 0) == None and row+1 < self.tableWidget.rowCount() and not self.tableWidget.item(row+1, 0) == None:
                resp = QtWidgets.QMessageBox.warning(MainWindow, "File Saving Error!", "There was error with saving a file. Please check your table it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                return
            if self.tableWidget.item(row, 1) == None and row+1< self.tableWidget.rowCount() and not self.tableWidget.item(row+1, 1) == None:
                resp = QtWidgets.QMessageBox.warning(MainWindow, "File Saving Error!", "There was error with saving a file. Please check your table it doesn't have any in-middle blank.", (QtWidgets.QMessageBox.Ok))
                return
            cat1.append(self.tableWidget.item(row, 0).text() if not self.tableWidget.item(row, 0) == None else '')
            cat2.append(self.tableWidget.item(row, 1).text() if not self.tableWidget.item(row, 1) == None else '')
            pass
        self.fileManager.writeData(cat1, cat2)
        self.SAVED = True
        self.EDITED = False
        self.CLEARED_EXTREMES = False
        self.updateStatusBar()
        pass

    def actionAddRowClicked(self):
        if not len(self.tableWidget.selectedIndexes()) == 0:
            selected_row_list = []
            selected_column_list = []
            for item in self.tableWidget.selectedIndexes():
                if selected_row_list.count(item.row()) == 0:
                    selected_row_list.append(item.row())
                    pass
                if selected_column_list.count(item.column()) == 0:
                    selected_column_list.append(item.column())
                    pass
                pass
            self.tableWidget.insertRow(max(selected_row_list)+1)
            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.tableWidget.setCurrentCell(max(selected_row_list)+1, max(selected_column_list))
            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
            pass
        else:
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            pass
        self.EDITED = True
        self.SAVED = False
        self.CLEARED_EXTREMES = False
        self.updateStatusBar()
        pass

    def actionDeleteRowsClicked(self):
        if not len(self.tableWidget.selectedIndexes()) == 0:
            selected_row_list = []
            for item in self.tableWidget.selectedIndexes():
                if selected_row_list.count(item.row()) == 0:
                    selected_row_list.append(item.row())
                    pass
                pass
            selected_row_list.sort()
            selected_row_list.reverse()
            for row in selected_row_list:
                self.tableWidget.removeRow(row)
                pass
            pass
        self.EDITED = True
        self.SAVED = False
        self.CLEARED_EXTREMES = False
        self.updateStatusBar()
        pass

    def actionDeleteAllClicked(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.EDITED = True
        self.SAVED = False
        self.CLEARED_EXTREMES = False
        self.updateStatusBar()
        pass

    def actionClearExtremesClicked(self):
        if not self.SAVED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, "The table isn't saved yet", "Save table first to check distribution chart!", (QtWidgets.QMessageBox.Ok))
            return
        cat1 = []
        cat2 = []
        cleared_cat1 = []
        cleared_cat2 = []
        for row in range(0, self.tableWidget.rowCount(), 1):
            if not self.tableWidget.item(row, 0) == None:
                cat1.append(float(self.tableWidget.item(row, 0).text()))
                pass
            if not self.tableWidget.item(row, 1) == None:
                cat2.append(float(self.tableWidget.item(row, 1).text()))
                pass
            pass
        if len(cat1) > 0 or len(cat2) > 0:
            if len(cat1) > 0:
                extremeManager1 = ExtremeManager(cat1)
                extremeManager1.setOffset(self.offset)
                cleared_cat1 = extremeManager1.clearExtremes()
                pass
            if len(cat2) > 0:
                extremeManager2 = ExtremeManager(cat2)
                extremeManager2.setOffset(self.offset)
                cleared_cat2 = extremeManager2.clearExtremes()
                pass
            self.tableWidget.setRowCount((len(cleared_cat1) if len(cleared_cat1) >= len(cleared_cat2) else len(cleared_cat2)))
            for row in range(0, (len(cleared_cat1) if len(cleared_cat1) >= len(cleared_cat2) else len(cleared_cat2)), 1):
                self.tableWidget.setItem(row,0, QtWidgets.QTableWidgetItem(str(cleared_cat1[row]) if not len(str(cleared_cat1[row])) == 0 else ''))
                self.tableWidget.setItem(row,1, QtWidgets.QTableWidgetItem(str(cleared_cat2[row]) if not len(str(cleared_cat2[row])) == 0 else ''))
                pass
            self.actionSaveClicked()
            self.EDITED = False
            self.SAVED = True
            self.CLEARED_EXTREMES = True
            self.updateStatusBar()
        else:
            resp = resp = QtWidgets.QMessageBox.warning(MainWindow, "Empty Table!", "Fill some data first before clearing extremes!", (QtWidgets.QMessageBox.Ok))
            pass
        pass

    def actionDisplayDataDistributionChartClicked(self):
        if not self.SAVED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, "The table isn't saved yet", "Save table first to check distribution chart!", (QtWidgets.QMessageBox.Ok))
            return
        else:
            if not self.CLEARED_EXTREMES:
                resp = QtWidgets.QMessageBox.question(MainWindow, "Uncleared Extreme Values!", "You didn't clear extreme values. Do you reallly want to check distribution chart right now?", (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No), QtWidgets.QMessageBox.No)
                if not resp == QtWidgets.QMessageBox.Yes:
                    return
                pass
            self.fileManager = FileManager(self.filename)
            cat1, cat2 = self.fileManager.loadData()
            manager = BAManager(cat1, cat2)
            manager.setCategoryName(1, self.catname1)
            manager.setCategoryName(2, self.catname2)
            manager.displayDataInChart(self.option)
            pass
        pass

    def actionDisplayBorderDistributionChartClicked(self):
        if not self.SAVED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, "The table isn't saved yet", "Save table first to check distribution chart!", (QtWidgets.QMessageBox.Ok))
            return
        elif not self.BORDER_CALCULATED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, "The Border value isn't calculated yet", "Calculate border value first to check distribution chart!", (QtWidgets.QMessageBox.Ok))
            return
        else:
            if not self.CLEARED_EXTREMES:
                resp = QtWidgets.QMessageBox.question(MainWindow, "Uncleared Extreme Values!", "You didn't clear extreme values. Do you reallly want to check distribution chart right now?", (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No), QtWidgets.QMessageBox.No)
                if not resp == QtWidgets.QMessageBox.Yes:
                    return
                pass
            self.fileManager = FileManager(self.filename)
            cat1, cat2 = self.fileManager.loadData()
            manager = BAManager(cat1, cat2)
            manager.border = self.border
            manager.setCategoryName(1, self.catname1)
            manager.setCategoryName(2, self.catname2)
            manager.displayBorderInChart(self.option)
            pass
        pass

    def actionEntropyBorderAlgorithmClicked(self):
        if not self.SAVED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, "The table isn't saved yet", "Save table first to check distribution chart!", (QtWidgets.QMessageBox.Ok))
            return
        else:
            if not self.CLEARED_EXTREMES:
                resp = QtWidgets.QMessageBox.question(MainWindow, "Uncleared Extreme Values!", "You didn't clear extreme values. Do you reallly want to calculate border right now?", (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No), QtWidgets.QMessageBox.No)
                if not resp == QtWidgets.QMessageBox.Yes:
                    return
                pass
            self.fileManager = FileManager(self.filename)
            cat1, cat2 = self.fileManager.loadData()
            manager = BAManager(cat1, cat2)
            manager.setStep(self.step)
            self.border = manager.calculateEntropyBorder()
            resp = QtWidgets.QMessageBox.information(MainWindow, "Border Calculation Complete!", "Calculated Entropy Border: " + str(self.border))
            self.BORDER_CALCULATED = True
            pass
        pass
    
    def actionSignedBorderAlgorithmClicked(self):
         if not self.SAVED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, "The table isn't saved yet", "Save table first to check distribution chart!", (QtWidgets.QMessageBox.Ok))
            return
         else:
            if not self.CLEARED_EXTREMES:
                resp = QtWidgets.QMessageBox.question(MainWindow, "Uncleared Extreme Values!", "You didn't clear extreme values. Do you reallly want to calculate border right now?", (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No), QtWidgets.QMessageBox.No)
                if not resp == QtWidgets.QMessageBox.Yes:
                    return
                pass
            self.fileManager = FileManager(self.filename)
            cat1, cat2 = self.fileManager.loadData()
            manager = BAManager(cat1, cat2)
            manager.setStep(self.step)
            self.border = manager.calculateSignedBorder()
            resp = QtWidgets.QMessageBox.information(MainWindow, "Border Calculation Complete!", "Calculated Signed Border: " + str(self.border))
            self.BORDER_CALCULATED = True
            pass
         pass

    def actionUnsignedBorderAlgorithmClicked(self):
         if not self.SAVED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, "The table isn't saved yet", "Save table first to check distribution chart!", (QtWidgets.QMessageBox.Ok))
            return
         else:
            if not self.CLEARED_EXTREMES:
                resp = QtWidgets.QMessageBox.question(MainWindow, "Uncleared Extreme Values!", "You didn't clear extreme values. Do you reallly want to calculate border right now?", (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No), QtWidgets.QMessageBox.No)
                if not resp == QtWidgets.QMessageBox.Yes:
                    return
                pass
            self.fileManager = FileManager(self.filename)
            cat1, cat2 = self.fileManager.loadData()
            manager = BAManager(cat1, cat2)
            manager.setStep(self.step)
            self.border = manager.calculateUnsignedBorder()
            resp = QtWidgets.QMessageBox.information(MainWindow, "Border Calculation Complete!", "Calculated Unsigned Border: " + str(self.border))
            self.BORDER_CALCULATED = True
            pass
         pass

    def actionSignedMeanBorderAlgorithmClicked(self):
         if not self.SAVED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, "The table isn't saved yet", "Save table first to check distribution chart!", (QtWidgets.QMessageBox.Ok))
            return
         else:
            if not self.CLEARED_EXTREMES:
                resp = QtWidgets.QMessageBox.question(MainWindow, "Uncleared Extreme Values!", "You didn't clear extreme values. Do you reallly want to calculate border right now?", (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No), QtWidgets.QMessageBox.No)
                if not resp == QtWidgets.QMessageBox.Yes:
                    return
                pass
            self.fileManager = FileManager(self.filename)
            cat1, cat2 = self.fileManager.loadData()
            manager = BAManager(cat1, cat2)
            manager.setStep(self.step)
            self.border = manager.calculateSignedMeanBorder()
            resp = QtWidgets.QMessageBox.information(MainWindow, "Border Calculation Complete!", "Calculated Signed-Mean Border: " + str(self.border))
            self.BORDER_CALCULATED = True
            pass
         pass

    def actionUnsignedMeanBorderAlgorithmClicked(self):
         if not self.SAVED:
            resp = QtWidgets.QMessageBox.warning(MainWindow, "The table isn't saved yet", "Save table first to check distribution chart!", (QtWidgets.QMessageBox.Ok))
            return
         else:
            if not self.CLEARED_EXTREMES:
                resp = QtWidgets.QMessageBox.question(MainWindow, "Uncleared Extreme Values!", "You didn't clear extreme values. Do you reallly want to calculate border right now?", (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No), QtWidgets.QMessageBox.No)
                if not resp == QtWidgets.QMessageBox.Yes:
                    return
                pass
            self.fileManager = FileManager(self.filename)
            cat1, cat2 = self.fileManager.loadData()
            manager = BAManager(cat1, cat2)
            manager.setStep(self.step)
            self.border = manager.calculateUnsignedMeanBorder()
            resp = QtWidgets.QMessageBox.information(MainWindow, "Border Calculation Complete!", "Calculated Unsigned-Mean Border: " + str(self.border))
            self.BORDER_CALCULATED = True
            pass
         pass

    def actionLicenseClicked(self):
        subprocess.Popen('pythonw license.pyw', shell=True)
        pass

    def actionCategory1Clicked(self):
        name, ok = QtWidgets.QInputDialog.getText(MainWindow,'Category 1 Name Option', 'Input Name of Category 1.')
        if ok:
            if len(name) > 0:
                self.catname1 = name
                pass
            self.updateTableLabel()
            pass
        pass

    def actionCategory2Clicked(self):
        name, ok = QtWidgets.QInputDialog.getText(MainWindow, 'Category 2 Name Option', 'Input Name of Category 2.')
        if ok:
            if len(name) > 0:
                self.catname2 = name
                pass
            self.updateTableLabel()
            pass
        pass

    def actionStepClicked(self):
        step, ok = QtWidgets.QInputDialog.getDouble(MainWindow, 'Border Step Option', 'Input step for calculating border.', 0.1, -2147483647, 2147483647, 5)
        if ok:
            if step > 0:
                self.step = step
                pass
            self.updateStatusBar()
            pass
        pass
    
    def actionDisplayModeClicked(self):
        mode, ok = QtWidgets.QInputDialog.getItem(MainWindow, 'Display Mode Option', 'Select chart display mode.', ['Unlayered', 'Layered'])
        if ok:
            if mode == 'Layered':
                self.option = BAManager.OPTION_LAYERED
                pass
            else:
                self.option = BAManager.OPTION_UNLAYERED
                pass
            self.updateStatusBar()
            pass
        pass

    def actionOffsetClicked(self):
        offset, ok = QtWidgets.QInputDialog.getDouble(MainWindow, 'Extreme Offset Option', 'Input offset for excluding extremes.', 10, -2147483647, 2147483647, 5)
        if ok:
            if offset > 0:
                self.offset = offset
                pass
            self.updateStatusBar()
            pass
        pass

    def actionUserHelpClicked(self):
        webbrowser.open("https://github.com/stevenoh0908/Dato/blob/master/doc/help.md")
        pass

    def actionExitClicked(self):
        exit()
        pass
    
    pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tableManager()
    ui.setupUi(MainWindow)
    ui.setupVariables()
    MainWindow.show()
    sys.exit(app.exec_())

