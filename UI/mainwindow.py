# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1166, 935)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../source/ico/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-2176, 0, 5000, 5000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.logLayout = QtWidgets.QVBoxLayout()
        self.logLayout.setObjectName("logLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(-20, -238, 5000, 5000))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.logLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.logLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1166, 23))
        self.menubar.setObjectName("menubar")
        self.Mfile = QtWidgets.QMenu(self.menubar)
        self.Mfile.setObjectName("Mfile")
        self.Mextractor = QtWidgets.QMenu(self.menubar)
        self.Mextractor.setObjectName("Mextractor")
        self.Mdetection = QtWidgets.QMenu(self.menubar)
        self.Mdetection.setObjectName("Mdetection")
        self.Mentropy = QtWidgets.QMenu(self.menubar)
        self.Mentropy.setObjectName("Mentropy")
        self.about = QtWidgets.QMenu(self.menubar)
        self.about.setObjectName("about")
        self.Mshow = QtWidgets.QMenu(self.menubar)
        self.Mshow.setObjectName("Mshow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../source/ico/addfile.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon1)
        self.open.setObjectName("open")
        self.save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../source/ico/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setObjectName("save")
        self.setpage = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../source/ico/设置.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setpage.setIcon(icon3)
        self.setpage.setObjectName("setpage")
        self.print = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../source/ico/打印文件.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print.setIcon(icon4)
        self.print.setObjectName("print")
        self.runextract = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../source/ico/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runextract.setIcon(icon5)
        self.runextract.setObjectName("runextract")
        self.extractorset = QtWidgets.QAction(MainWindow)
        self.extractorset.setObjectName("extractorset")
        self.rundetection = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../source/ico/play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rundetection.setIcon(icon6)
        self.rundetection.setObjectName("rundetection")
        self.detectionset = QtWidgets.QAction(MainWindow)
        self.detectionset.setObjectName("detectionset")
        self.entropyset = QtWidgets.QAction(MainWindow)
        self.entropyset.setObjectName("entropyset")
        self.aboutqrng = QtWidgets.QAction(MainWindow)
        self.aboutqrng.setObjectName("aboutqrng")
        self.aboutqt = QtWidgets.QAction(MainWindow)
        self.aboutqt.setObjectName("aboutqt")
        self.show = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../source/ico/运行.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show.setIcon(icon7)
        self.show.setObjectName("show")
        self.showset = QtWidgets.QAction(MainWindow)
        self.showset.setObjectName("showset")
        self.Mfile.addAction(self.open)
        self.Mfile.addSeparator()
        self.Mfile.addAction(self.save)
        self.Mfile.addAction(self.setpage)
        self.Mfile.addAction(self.print)
        self.Mextractor.addAction(self.runextract)
        self.Mextractor.addAction(self.extractorset)
        self.Mdetection.addAction(self.rundetection)
        self.Mdetection.addAction(self.detectionset)
        self.Mentropy.addAction(self.entropyset)
        self.about.addAction(self.aboutqrng)
        self.about.addAction(self.aboutqt)
        self.Mshow.addAction(self.show)
        self.Mshow.addAction(self.showset)
        self.menubar.addAction(self.Mfile.menuAction())
        self.menubar.addAction(self.Mextractor.menuAction())
        self.menubar.addAction(self.Mdetection.menuAction())
        self.menubar.addAction(self.Mentropy.menuAction())
        self.menubar.addAction(self.Mshow.menuAction())
        self.menubar.addAction(self.about.menuAction())
        self.toolBar.addAction(self.open)
        self.toolBar.addAction(self.save)
        self.toolBar.addAction(self.runextract)
        self.toolBar.addAction(self.rundetection)
        self.toolBar.addAction(self.show)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open.setShortcut('Ctrl+O')
        self.open.triggered.connect(self.openfile)
        self.save.setShortcut('Ctrl+s')
        self.save.triggered.connect(self.savefile)
        self.setpage.setShortcut('Ctrl+P')
        self.setpage.triggered.connect(self.pagesettings)
        self.print.setShortcut('Ctrl+s')
        self.print.triggered.connect(self.printdialog)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "随机数发生器"))
        self.label.setText(_translate("MainWindow", "程序日志"))
        self.Mfile.setTitle(_translate("MainWindow", "文件"))
        self.Mextractor.setTitle(_translate("MainWindow", "提取"))
        self.Mdetection.setTitle(_translate("MainWindow", "检测"))
        self.Mentropy.setTitle(_translate("MainWindow", "熵源"))
        self.about.setTitle(_translate("MainWindow", "关于"))
        self.Mshow.setTitle(_translate("MainWindow", "展示"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.open.setText(_translate("MainWindow", "打开原始序列文件"))
        self.save.setText(_translate("MainWindow", "设置输出文件位置"))
        self.setpage.setText(_translate("MainWindow", "页面设置"))
        self.print.setText(_translate("MainWindow", "打印文件"))
        self.runextract.setText(_translate("MainWindow", "运行提取"))
        self.extractorset.setText(_translate("MainWindow", "提取设置"))
        self.rundetection.setText(_translate("MainWindow", "运行检测"))
        self.detectionset.setText(_translate("MainWindow", "检测设置"))
        self.detectionset.setIconText(_translate("MainWindow", "检测设置"))
        self.entropyset.setText(_translate("MainWindow", "熵源设置"))
        self.aboutqrng.setText(_translate("MainWindow", "关于QRNG"))
        self.aboutqt.setText(_translate("MainWindow", "关于Qt"))
        self.show.setText(_translate("MainWindow", "展示结果"))
        self.showset.setText(_translate("MainWindow", "结果展示设置"))



    def openfile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'open', '.\\', "Images (*.png *.csv *txt *.jpg)")
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def savefile(self):
        fileName = QFileDialog.getSaveFileName(self, '保存文件', './', "Text files (*.txt)")
        if fileName[0]:
            with open(fileName[0], 'w', encoding='gb18030', errors='ignore') as f:
                f.write(self.tx.toPlainText())


    def pagesettings(self):
        printsetdialog = QPageSetupDialog(self.printer, self)
        printsetdialog.exec_()


    def printdialog(self):
        printdialog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printdialog.exec_():
            self.tx.print(self.printer)








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())