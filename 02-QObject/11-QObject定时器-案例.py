from PyQt5.QtWidgets import QLabel,QApplication,QWidget
from PyQt5.QtCore import QObject
import sys

class MyObject(QObject):
    def timerEvent(self,evt):
        print(evt,"1")


class MyLabel(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setText("10")
        self.move(200,200)
        self.setStyleSheet("font-size:25px")

    def set_sec(self,sec):
        self.setText(str(sec))

    def start_my_timer(self,ms):                               # 首先要启动定时器
        self.timer_id = self.startTimer(ms)  # 继承于QObject

    def timerEvent(self,*args,**kwargs):                       # 其次要有定时器的事件
        print("XXX")
         # 1.获取标签内容
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))

        if current_sec == 0:
            print("停止")
            self.killTimer(self.timer_id)

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QObject定时器案例")
window.setGeometry(400,250,500,500)

label = MyLabel(window)
label.set_sec(10)
label.start_my_timer(1000)

window.show()

sys.exit(app.exec_())





