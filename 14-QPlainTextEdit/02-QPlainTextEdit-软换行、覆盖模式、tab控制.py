import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit")
        self.resize(500, 500)
        self.move(400, 250)
        self.setup_ui()

    def setup_ui(self):
        test_btn = QPushButton("测试按钮",self)
        test_btn.move(20,20)
        pte = QPlainTextEdit(self)
        self.pte = pte
        pte.move(100,100)
        pte.resize(300,300)


        # ------自动换行------------------------
        print(pte.lineWrapMode())  # 默认值为False 循环模式->自动换行
        pte.setLineWrapMode(QPlainTextEdit.NoWrap)  # 取消自动换行
        """
        NoWrap = 0
        WidgetWidth = 1
        """ 



        # -------覆盖模式--------  指的是：文本光标变成了 黑方块，会替换掉覆盖的内容
        print(pte.overwriteMode())  # 默认为False
        pte.setOverwriteMode(True)  # 设置单个字符，对中文支持不佳


        # -------tab控制-------
        # pte.setTabChangesFocus(True)  # 将tab键功能改为切换焦点， 在本列中表现为焦点 有 无
        pte.setTabChangesFocus(False)  # 将tab键功能改为插入制表符
        pte.setTabStopDistance(10)  # 控制tab缩进距离


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())