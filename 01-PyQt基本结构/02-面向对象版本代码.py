import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication

class Window(QWidget):
    
    def __init__(self):
        super().__init__()  # 进行父类的初始化
        self.setWindowTitle("面向对象版本的PyQt代码")
        self.resize(500, 500)
        self.move(400, 250) 


    def setup_ui(self):
        label = QLabel(self)
        label.setText("Hello World")
        label.move(200,240)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.setup_ui()   # 设置窗内的所有子控件
    window.show()  # 把window显示出来

    sys.exit(app.exec_())

