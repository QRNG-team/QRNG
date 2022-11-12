from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget ,QPushButton ,QTextEdit ,QVBoxLayout ,QFileDialog ,QDialog
from PyQt5.QtPrintSupport import QPrinter ,QPrintDialog ,QPageSetupDialog

import sys

class printDialogDemo(QWidget):
    def __init__(self):
        super(printDialogDemo, self).__init__()

        # 创建打印机对象
        self.printer = QPrinter()

        # 创建三个按钮
        self.btn1 = QPushButton("打开文件") # 打开文件并且将文件内容显示在TextEdit中
        self.btn2 = QPushButton("弹出打印设置窗口") # 弹出打印设置窗口
        self.btn3 = QPushButton("打印") # 进行打印

        # 创建文本框，用于显示打印的文本内容
        self.textEdit = QTextEdit()

        # 设置垂直布局将控件放入
        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.textEdit)

        # 将布局设置在窗口
        self.setLayout(layout)
        self.setWindowTitle("利用PyQt5进行文件打印")

        # 按钮设置槽函数
        self.btn1.clicked.connect(self.openFile)
        self.btn2.clicked.connect(self.showSettingsDialog)
        self.btn3.clicked.connect(self.showPrintDialog)

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self ,"打开文件" ,".")
        if fname[0]:
            # 打开文件，将文件的内容显示在文本框中
            with open(fname[0] ,'r' ,encoding="utf-8") as f:
                self.textEdit.setText(f.read())

    def showSettingsDialog(self):
        settingsDialog = QPageSetupDialog(self.printer ,self) # 在当前窗口针对打印机对象弹出设置对话框
        settingsDialog.exec() # 循环

    def showPrintDialog(self):
        printerDialog = QPrintDialog(self.printer ,self) # 在当前窗口针对打印机对象弹出打印对话框
        # printerDialog.exec()表示等待用户的操作，QDialog.Accepted表示用户操作了类似于确认的操作，当用户的操作时确认的操作时，执行if下面的语句
        if QDialog.Accepted == printerDialog.exec():
            self.textEdit.print(self.printer)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = printDialogDemo()
    mainWin.show()
    app.exec_()