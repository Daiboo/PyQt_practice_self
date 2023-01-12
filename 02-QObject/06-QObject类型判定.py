from PyQt5.QtWidgets import QWidget,QPushButton,QLabel,QApplication
from PyQt5.QtCore import QObject
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QObject类型判定")
        self.setGeometry(400,250,500,500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject类型判定()

    def QObject类型判定(self):
        obj = QObject()
        w = QWidget()
        btn = QPushButton()
        label = QLabel()

        objs = [obj,w,btn,label]

        for o in objs:
            print(o,"是否为控件",o.isWidgetType())
            print(o.inherits("QWidget"))  # 对象是否继承自Qwidget
            print(o.inherits("QPushButton"))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())


    

        