import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("交互状态案例")
        self.resize(500,500)
        self.move(400,250)
        self.setup_ui()

    def setup_ui(self):
        # 添加三个子控件
        label = QLabel(self)
        label.move(100,50)
        label.hide()

        le = QLineEdit(self)
        le.move(100,100)

        btn = QPushButton(self)
        btn.setText("登录")
        btn.move(100,150)
        btn.setEnabled(False)  # 先设置按钮不可用

        def text_cao(text):
            """若文本le中的内容改变且非空,则设置按钮为btn可用"""
            btn.setEnabled(len(text) > 0)  # 此槽函数需要接收textChanged返回的参数，不能设为匿名函数

        le.textChanged[str].connect(text_cao)

        def check():
            "登录按钮功能的槽函数"
            content = le.text()

            # 判定是否为muzing
            # 是->显示之前隐藏的提示标签，展示文本
            label.setText("登录成功") if content == "muzing" else label.setText("登录失败")
            label.adjustSize()  # 调整label尺寸，适应不同文本内容，保证显示
            label.show()

        btn.pressed.connect(check)

app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec_())


