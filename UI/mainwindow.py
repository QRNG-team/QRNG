# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtPrintSupport import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow
from UI import *
from extractor import mainextractor, ottoeplitz, plotting
from extractor.mainextractor import Extractor
from UI.Thread import *
from UI import extractorset, detectionset, entropyset
import Tool.glo as glo


class Ui_MainWindow(object):
    """
    主界面生成代码，借助扩展工具PyUIC将.ui转成
    """

    def __init__(self):
        self.thread = None
        self.thread_1 = None
        self.N = 0
        self.scale = 0
        self.fername = None  # 待提取文件
        self.fewname = None  # 提取结果文件
        self.filename = None  # 文件
        self.fdrname = None  # 待检测文件
        self.fdwname = None  # 检测结果文件
        self.faname = None  # 待评估文件
        self.printer = QPrinter()
        self.entropylist = [0, 0, 0, 0]
        self.entropypara = [0, 0, 0]
        self.standard = True
        self.countEntropy = 0
        self.extractlist = [0, 0, 0, 0]
        # 一定要在主窗口类的初始化函数中对子窗口进行实例化，如果在其他函数中实例化子窗口
        # 可能会出现子窗口闪退的问题

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1241, 968)
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
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 5000, 5000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ResultBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.ResultBrowser.setFont(font)
        self.ResultBrowser.setObjectName("ResultBrowser")
        self.horizontalLayout_3.addWidget(self.ResultBrowser)
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
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 5000, 5000))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LogBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.LogBrowser.setFont(font)
        self.LogBrowser.setObjectName("LogBrowser")
        self.horizontalLayout_4.addWidget(self.LogBrowser)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.logLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.logLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1241, 23))
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
        self.openextract = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../source/ico/addfile.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openextract.setIcon(icon1)
        self.openextract.setObjectName("openextract")
        self.getextractfolder = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../source/ico/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getextractfolder.setIcon(icon2)
        self.getextractfolder.setObjectName("getextractfolder")
        self.setpage = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../source/ico/setup.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../source/ico/设置.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extractorset.setIcon(icon6)
        self.extractorset.setObjectName("extractorset")
        self.rundetection = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../source/ico/检测.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rundetection.setIcon(icon7)
        self.rundetection.setObjectName("rundetection")
        self.detectionset = QtWidgets.QAction(MainWindow)
        self.detectionset.setIcon(icon6)
        self.detectionset.setObjectName("detectionset")
        self.entropyset = QtWidgets.QAction(MainWindow)
        self.entropyset.setIcon(icon6)
        self.entropyset.setObjectName("entropyset")
        self.aboutqrng = QtWidgets.QAction(MainWindow)
        self.aboutqrng.setObjectName("aboutqrng")
        self.aboutqt = QtWidgets.QAction(MainWindow)
        self.aboutqt.setObjectName("aboutqt")
        self.show = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../source/ico/展示.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show.setIcon(icon8)
        self.show.setObjectName("show")
        self.showset = QtWidgets.QAction(MainWindow)
        self.showset.setIcon(icon6)
        self.showset.setObjectName("showset")
        self.getdetectfolder = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../source/ico/文件设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getdetectfolder.setIcon(icon9)
        self.getdetectfolder.setObjectName("getdetectfolder")
        self.opendetection = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../source/ico/打开文件夹.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.opendetection.setIcon(icon10)
        self.opendetection.setObjectName("opendetection")
        self.openAccess = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../source/ico/打开文件.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openAccess.setIcon(icon11)
        self.openAccess.setObjectName("openAccess")
        self.runaccess = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../source/ico/评估.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runaccess.setIcon(icon12)
        self.runaccess.setObjectName("runaccess")

        self.Mfile.addAction(self.openextract)
        self.Mfile.addAction(self.opendetection)
        self.Mfile.addAction(self.openAccess)
        self.Mfile.addSeparator()
        self.Mfile.addAction(self.getdetectfolder)
        self.Mfile.addAction(self.getextractfolder)
        self.Mfile.addSeparator()
        self.Mfile.addAction(self.setpage)
        self.Mfile.addAction(self.print)
        self.Mextractor.addAction(self.runextract)
        self.Mextractor.addAction(self.extractorset)
        self.Mdetection.addAction(self.rundetection)
        self.Mdetection.addAction(self.detectionset)
        self.Mentropy.addAction(self.entropyset)
        self.Mentropy.addAction(self.runaccess)
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
        self.toolBar.addAction(self.openextract)
        self.toolBar.addAction(self.opendetection)
        self.toolBar.addAction(self.openAccess)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.getextractfolder)
        self.toolBar.addAction(self.getdetectfolder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.runextract)
        self.toolBar.addAction(self.rundetection)
        self.toolBar.addAction(self.runaccess)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.show)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """
          设置快捷键并通过信号-槽机制触发事件
        """
        self.openextract.setShortcut('Ctrl+shift+E')
        self.openextract.triggered.connect(self.openExtractFile)
        self.opendetection.setShortcut('Ctrl+shift+D')
        self.opendetection.triggered.connect(self.openDetectionFile)
        self.opendetection.setShortcut('Ctrl+shift+A')
        self.openAccess.triggered.connect(self.openAccessFile)
        self.getextractfolder.triggered.connect(self.getExtractFolder)
        self.getdetectfolder.triggered.connect(self.getDetectionFolder)
        self.setpage.setShortcut('Ctrl+P')
        self.setpage.triggered.connect(self.pageSettings)
        self.print.triggered.connect(self.printDialog)
        self.runextract.setShortcut('Ctrl+E')
        self.runextract.triggered.connect(self.runExtract)
        self.rundetection.setShortcut('Ctrl+D')
        self.rundetection.triggered.connect(self.runDetection)
        self.runaccess.setShortcut('Ctrl+A')
        self.runaccess.triggered.connect(self.runAccess)
        self.extractorset.triggered.connect(self.extractorSet)
        self.detectionset.triggered.connect(self.detectionSet)
        self.entropyset.triggered.connect(self.entropySet)

        glo._init()  # 先必须在主模块初始化（只在Main模块需要一次即可）
        # 定义跨模块全局变量

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "随机数发生器"))
        self.label.setText(_translate("MainWindow", "程序日志"))
        self.Mfile.setTitle(_translate("MainWindow", "文件"))
        self.Mextractor.setTitle(_translate("MainWindow", "提取"))
        self.Mdetection.setTitle(_translate("MainWindow", "检测"))
        self.Mentropy.setTitle(_translate("MainWindow", "熵评估"))
        self.about.setTitle(_translate("MainWindow", "关于"))
        self.Mshow.setTitle(_translate("MainWindow", "展示"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.openextract.setText(_translate("MainWindow", "打开原始序列文件"))
        self.getextractfolder.setText(_translate("MainWindow", "设置输出文件位置"))
        self.setpage.setText(_translate("MainWindow", "页面管理"))
        self.print.setText(_translate("MainWindow", "打印文件"))
        self.runextract.setText(_translate("MainWindow", "运行提取"))
        self.extractorset.setText(_translate("MainWindow", "提取设置"))
        self.rundetection.setText(_translate("MainWindow", "运行检测"))
        self.detectionset.setText(_translate("MainWindow", "检测设置"))
        self.detectionset.setIconText(_translate("MainWindow", "检测设置"))
        self.entropyset.setText(_translate("MainWindow", "熵评估设置"))
        self.runaccess.setText(_translate("MainWindow", "运行评估"))
        self.aboutqrng.setText(_translate("MainWindow", "关于QRNG"))
        self.aboutqt.setText(_translate("MainWindow", "关于Qt"))
        self.show.setText(_translate("MainWindow", "展示结果"))
        self.showset.setText(_translate("MainWindow", "结果展示设置"))
        self.getdetectfolder.setText(_translate("MainWindow", "设置检测文件路径"))
        self.opendetection.setText(_translate("MainWindow", "打开待检测文件"))
        self.openAccess.setText(_translate("MainWindow", "打开待评估文件"))

    def openExtractFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'open', '.\\', "Images (*.png *.csv *txt *.jpg)")
        # if fname[0]:
        #     f = open(fname[0], 'r')
        #     with f:
        #         data = f.read()
        if len(fname[0]):
            self.LogBrowser.append(f"已成功导入待提取文件：{fname[0]}")
        # l = fname[0].rsplit('/', 1)
        # print(l)
        self.fername = fname[0]
        self.filename = "extract"
        # self.filename = l[1]

    def openDetectionFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'open', '.\\', "Images (*.png *.csv *txt *.jpg)")
        # if fname[0]:
        #     f = open(fname[0], 'r')
        #     with f:
        #         data = f.read()
        if len(fname[0]):
            self.LogBrowser.append(f"已成功导入待检测文件：{fname[0]}")
        # l = fname[0].rsplit('/',1)
        # print(l)
        self.fdrname = fname[0]
        self.filename = "detection"
        # self.filename = l[-1]

    def openAccessFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'open', '.\\', "Images (*.png *.csv *txt *.jpg)")
        # if fname[0]:
        #     f = open(fname[0], 'r')
        #     with f:
        #         data = f.read()
        if len(fname[0]):
            self.LogBrowser.append(f"已成功导入待评估文件：{fname[0]}")
        # l = fname[0].rsplit('/', 1)
        # print(l)
        self.faname = fname[0]
        self.filename = "Access"
        # self.filename = l[1]

    def extractorSet(self):  # 提取设置窗口
        self.exwin = extractorset.Ui_exwin(self.extractlist, self.countEntropy)
        # 连接信号
        self.exwin.signal.connect(self.getexwin)
        self.exwin.show()

    def getexwin(self, lst, para):  # 接收提取设置和熵评估计算设置
        self.extractlist = lst
        self.countEntropy = para

    def detectionSet(self):  # 检测设置窗口
        # 连接信号
        self.exdec = detectionset.Ui_exdec(self.standard)
        self.exdec.signal.connect(self.getdetectwin)
        self.exdec.show()
        # self._signal.emit(self.entropylist, self.entropypara)

    def getdetectwin(self, standard):  # 接收用户所选择的检测标准
        self.standard = standard
        if self.standard:
            self.LogBrowser.append(f"已选择随机数检测标准为：NIST SP800-22r1a")
        else:
            self.LogBrowser.append(f"已选择随机数检测标准为：国密GM/T 0005-2021")
        print(standard)

    def entropySet(self):  # 评估设置窗口
        self.accesswin = entropyset.Ui_widget(self.entropylist, self.entropypara)
        # 连接信号
        self.accesswin.signal.connect(self.getaccesswin)
        self.accesswin.show()

    def getaccesswin(self, lst, para):  # 接收熵评估计算选择和参数
        self.entropylist = lst
        self.entropypara = para
        print(lst, para)
        ans1 = "最小熵"
        ans2 = "香农熵"
        ans3 = "样本熵"
        ans4 = "瑞丽熵"
        p1 = "embedding dimension"
        p2 = "tolerance"
        p3 = "order"
        entropyAns = ""
        paraAns = ""
        if self.entropylist[0]:
            entropyAns = entropyAns + ans1 + " "
        if self.entropylist[1]:
            entropyAns = entropyAns + ans2 + " "
        if self.entropylist[2]:
            entropyAns = entropyAns + ans3 + " "
            paraAns = paraAns + p1 + "=" + str(self.entropypara[0]) + "; "
            paraAns = paraAns + p2 + "=" + str(self.entropypara[1]) + "; "
        if self.entropylist[3]:
            entropyAns = entropyAns + ans4 + " "
            paraAns = paraAns + p3 + "=" + str(self.entropypara[2]) + "; "
        self.LogBrowser.append(f"已选择熵评估种类为{entropyAns}")
        self.LogBrowser.append(f"所选择的熵参数为{paraAns}")

    def getExtractFolder(self):
        self.fewname = QtWidgets.QFileDialog.getExistingDirectory()
        if len(self.fewname):
            self.LogBrowser.append(f"输出序列结果所在文件夹已设置为{self.fewname}")

    def getDetectionFolder(self):
        self.fdwname = QtWidgets.QFileDialog.getExistingDirectory()
        if len(self.fdwname):
            self.LogBrowser.append(f"检测结果所在文件夹已设置为{self.fdwname}")

    def pageSettings(self):
        print(1)
        printsetdialog = QPageSetupDialog(self.printer, self)
        printsetdialog.exec_()

    def printDialog(self):
        printdialog = QPrintDialog(self.printer, self)
        if QPrintDialog.Accepted == printdialog.exec_():
            self.tx.print(self.printer)

    def runExtract(self):
        if self.fername is None:
            self.LogBrowser.append(f"提取文件不能为空")
            return
        if self.fewname is None:
            self.LogBrowser.append(f"输出提取结果文件路径不能为空")
            return
        self.LogBrowser.append(f"正在提取{self.fername}")
        self.scale = 2 ** 18 + 20000
        self.N = 14  # 实验数据类型
        para = {"fername": self.fername, "fewname": self.fewname, "scale": self.scale, "N": self.N,
                "fdrname": self.fdrname, "fdwname": self.fdwname,
                "filename": self.filename}
        print('Start clicked.')
        glo.set_value('extractbar', 0)  # 进度条进度设置，采用跨文件全部变量
        self.runextract.setEnabled(False)
        self.createProgressBar()
        self.is_done = 0  # 设置完成标记 完成/未完成 1/0
        self.thread_1 = Runthread(1)
        self.thread_1.progressBarValue.connect(self.callback)
        self.thread_1.signal_done.connect(self.callback_done)
        self.thread_1.start()
        self.thread = Extract_Thread(para)  # 将线程thread的信号finishSignal和UI主线程中的槽函数Change进行连接
        self.thread.finishSignal.connect(self.ExtractEnd)
        # 启动线程，执行线程类中run函数
        self.thread.start()

    def runDetection(self):
        if self.fdrname is None:
            self.LogBrowser.append(f"检测文件不能为空")
            return
        if self.fdwname is None:
            self.LogBrowser.append(f"输出检测结果文件路径不能为空")
            return
        self.LogBrowser.append(f"正在检测{self.fdrname}")
        self.scale = 2 ** 18 + 20000
        self.N = 14  # 实验数据类型
        para = {"fername": self.fername, "fewname": self.fewname, "scale": self.scale, "N": self.N,
                "fdrname": self.fdrname, "fdwname": self.fdwname,
                "filename": self.filename}
        if self.standard:
            self.LogBrowser.append('正在使用 NIST SP800-22r1a随机数检测标准 对随机数文件进行检测')
            print('Start clicked.')
            glo.set_value('detectbar', 0)
            self.rundetection.setEnabled(False) #控件不可交互
            self.createProgressBar()
            self.is_done = 0  # 设置完成标记 完成/未完成 1/0
            self.thread_1 = Runthread(2)
            self.thread_1.progressBarValue.connect(self.callback)
            self.thread_1.signal_done.connect(self.callback_done)
            self.thread_1.start()
            self.thread = Detection_Thread(para, self.standard)  # 将线程thread的信号finishSignal和UI主线程中的槽函数进行连接
            self.thread.finishSignal.connect(self.DetectionEnd)
            # 启动线程，执行线程类中run函数
            self.thread.start()
        else:
            self.LogBrowser.append('正在使用 国密GM/T 0005-2021随机数检测标准 对随机数文件进行检测')
            print('Start clicked.')
            glo.set_value('detectbar2', 0)
            self.rundetection.setEnabled(False)   #控件不可交互
            self.createProgressBar()
            self.is_done = 0  # 设置完成标记 完成/未完成 1/0
            self.thread_1 = Runthread(4)
            self.thread_1.progressBarValue.connect(self.callback)
            self.thread_1.signal_done.connect(self.callback_done)
            self.thread_1.start()
            self.thread = Detection_Thread(para, self.standard)  # 将线程thread的信号finishSignal和UI主线程中的槽函数进行连接
            self.thread.fb.connect(self.Detection2_End)
            # 启动线程，执行线程类中run函数
            self.thread.start()

    def runAccess(self):
        if self.faname is None:
            self.LogBrowser.append(f"评估文件不能为空")
            return
        self.LogBrowser.append(f"正在评估{self.faname}")
        print('Start clicked.')
        glo.set_value('accessbar', 0)  # 进度条进度设置，采用跨文件全部变量
        self.runaccess.setEnabled(False)
        self.createProgressBar()
        self.is_done = 0  # 设置完成标记 完成/未完成 1/0
        self.thread_1 = Runthread(3)
        self.thread_1.progressBarValue.connect(self.callback)
        self.thread_1.signal_done.connect(self.callback_done)
        self.thread_1.start()
        self.thread = Access_Thread(self.entropylist,
                                    self.entropypara, self.faname)  # 将线程thread的信号finishSignal和UI主线程中的槽函数Change进行连接
        self.thread.finishSignal.connect(self.AccessEnd)
        # 启动线程，执行线程类中run函数
        self.thread.start()

    # 接受通过emit传来的信息，执行相应操作
    def ExtractEnd(self, lst):
        print(lst)
        self.LogBrowser.append(lst[-1])
        self.ResultBrowser.append('原始数据最小熵为： %.2f \n' % lst[0])
        self.ResultBrowser.append('提取运行时间为： %.2f秒 \n' % lst[1])
        self.ResultBrowser.append('提取速度为： %.2fkbps\n' % lst[2])
        self.ResultBrowser.ensureCursorVisible()
        self.LogBrowser.append(f"完成提取")
        self.deleteProgressBar()

        self.runextract.setEnabled(True)

    def DetectionEnd(self, lst):
        self.LogBrowser.append(lst[-1])
        self.ResultBrowser.append('NIST检测结果如下：')
        self.ResultBrowser.append('{:<50s}{:<50s}{:<50s}'.format('test item', 'P-value', 'Result'))
        for i in range(len(lst) - 2):
            self.ResultBrowser.append('{:<50s} {:<50s}{:<50s}'.format(lst[i][0], lst[i][1], lst[i][2]))
        self.ResultBrowser.append('检测时间为： %.2f秒 ' % lst[-2])
        self.ResultBrowser.ensureCursorVisible()
        self.LogBrowser.append(f"完成NIST检测")
        self.deleteProgressBar()
        self.rundetection.setEnabled(True)

    def Detection2_End(self, fd, testtime):
        print("hh")
        self.LogBrowser.append(f"国密检测结果已保存到{fd}]")
        with open(f"{fd}") as f:
            for line in f.readlines():
                self.ResultBrowser.append(line)
        self.ResultBrowser.append('检测时间为： %.2f秒 ' % testtime)
        self.ResultBrowser.ensureCursorVisible()
        self.LogBrowser.append(f"完成国密检测")
        self.deleteProgressBar()
        self.rundetection.setEnabled(True)

    def AccessEnd(self, lst):
        self.LogBrowser.append(lst[-1])
        self.ResultBrowser.append('量子随机数熵评估结果如下：')
        for i in range(len(lst) - 1):
            self.ResultBrowser.append(lst[i])
        self.ResultBrowser.ensureCursorVisible()
        self.LogBrowser.append(f"完成评估")
        self.deleteProgressBar()
        self.rundetection.setEnabled(True)

    # def initExtractThread(self):
    #     # 创建子线程并和当前窗口绑定
    #     self.thread = ExtractThread(None)
    #
    #     self.send_singal.emit([self.frname,self.fwname,self.scale,self.N,self.filename])
    #     # 完成循环后删除子线程
    #     self.thread.finished.connect(self.thread.deleteLater)
    #     self.thread.send_singal.connect(self.change_value)

    def createProgressBar(self):
        # 设置进度条
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.progressBar.setValue(0)

    def deleteProgressBar(self):
        # 删除进度条
        self.progressBar.close()

    # 回传进度条参数
    def callback(self, i):
        self.progressBar.setValue(i)

    # 回传结束信号
    def callback_done(self, i):
        self.is_done = i
        # if self.is_done == 1:
        #     Runthread.ExeMessageDialog()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
