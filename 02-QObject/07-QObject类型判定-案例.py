from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QApplication
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QObject类型判定")
        self.setGeometry(400,400,500,500)
        self.setup_ui()

    def setup_ui(self):
        self.name()

    def name(self):
        label1 = QLabel(self)
        label1.setText("这是label1")
        label1.move(100,100)

        label2 = QLabel("这是label2",self)
        label2.move(200,100)

        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(100, 200)

        for widget in self.children():   # 获取到子类
            if widget.inherits("QLabel"):
                print(widget,"是")
                widget.setStyleSheet("background-color:cyan;")
            else:
                print(widget,"否")
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())          

        

