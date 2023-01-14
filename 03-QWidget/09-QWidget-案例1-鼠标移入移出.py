from PyQt5.QtWidgets import QLabel,QApplication,QWidget 
import sys


class MyLabel(QLabel): 
    def enterEvent(self,*args, **kwargs):  # 重写鼠标进入事件
        print("鼠标进入")
        self.setText("欢迎光临")

    def leaveEvent(self,*args, **kwargs):  # 重写鼠标移出事件
        print("鼠标离开")
        self.setText("谢谢惠顾")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("鼠标移入移出")
window.setGeometry(400,250,500,500)


label = MyLabel(window)
label.resize(200,200)
label.move(100,100)
label.setStyleSheet("background-color:cyan;")

window.show()
sys.exit(app.exec_())

