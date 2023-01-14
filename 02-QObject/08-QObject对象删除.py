import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QObject

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QObject对象删除")
        self.setGeometry(400,250,500,500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject对象删除()

    def QObject对象删除(self):
        # 删除一个对象时，也会解除与父对象的关系

        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        obj3 = QObject()

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda:print("obj1被释放了"))
        obj2.destroyed.connect(lambda:print("obj2被释放了"))
        obj3.destroyed.connect(lambda:print("obj3被释放了"))

        obj2.deleteLater()  # 在下一次消息循环才销毁  删除obj2，也会删除obj3
        print(obj1.children())  # 默认会获得所有子孩子
        print(obj2)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
 