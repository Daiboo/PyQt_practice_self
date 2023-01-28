import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox-数据获取")
        self.resize(500,500)
        self.move(400,250)
        self.setup_ui()

    def setup_ui(self):
        cbb = QComboBox(self)
        cbb.move(100,100)
        cbb.resize(150,20)
        cbb.addItems([str(x) for x in range(4)])
        cbb.addItem("字符串",{"name":"muzing"})
        btn = QPushButton("测试按钮",self)
        btn.move(100,200)
        
        btn.clicked.connect(lambda:cbb.count())
        btn.clicked.connect(lambda:print(f"当前Index为{cbb.currentIndex()}"))
        btn.clicked.connect(lambda:print(f"当前Date为{cbb.currentData()}"))
        btn.clicked.connect(lambda:print(f"当前Icon为{cbb.itemIcon(cbb.currentIndex())}"))
        btn.clicked.connect(
            lambda:print(f"最后一项Text为{cbb.itemText(cbb.count()-1)}")
        )



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
