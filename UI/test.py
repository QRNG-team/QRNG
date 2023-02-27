import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class InputDialogDemo(QWidget):
    def __init__(self,parent=None):
        super(InputDialogDemo, self).__init__(parent)

        #表单布局
        layout=QFormLayout()

        #创建按钮，当行文本框并建立按钮点击与槽函数的联系，添加到布局中
        self.btn1=QPushButton('获得列表里的选项')
        self.btn1.clicked.connect(self.getItem)
        self.Le1=QLineEdit()

        layout.addRow(self.btn1,self.Le1)

        # 创建按钮，当行文本框并建立按钮点击与槽函数的联系，添加到布局中
        self.btn2=QPushButton('获得字符串')
        self.btn2.clicked.connect(self.getText)
        self.le2=QLineEdit()
        layout.addRow(self.btn2,self.le2)

        # 创建按钮，当行文本框并建立按钮点击与槽函数的联系，添加到布局中
        self.btn3 = QPushButton('获得整数')
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()
        layout.addRow(self.btn3, self.le3)

        #设置主窗口的布局及标题
        self.setLayout(layout)
        self.setWindowTitle('Input Dialog例子')
    def getItem(self):
        #创建元组并定义初始值
        items=('C','C++','C#','JAva','Python')
        #获取item输入的值，以及ok键的点击与否（True 或False）
        #QInputDialog.getItem(self,标题,文本,元组,元组默认index,是否允许更改)
        item,ok=QInputDialog.getItem(self,"select input dialog",'语言列表',items,0,False)

        if ok and item:
            #满足条件时，设置单行文本框的文本
            self.Le1.setText(item)
    def getText(self):
        text,ok=QInputDialog.getText(self,'Text Input Dialog','输入姓名：')
        if ok:
            self.le2.setText(str(text))

    def getInt(self):
        num,ok=QInputDialog.getInt(self,'Integer input dualog','输入数字')
        if ok:
            self.le3.setText(str(num))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
