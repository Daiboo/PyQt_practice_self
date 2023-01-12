from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import QObject
import sys

class MyObject(QObject):
    def timerEvent(self,evt):
        print(evt,"1")
    

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QObect定时器的使用")
window.resize(500,500)
window.move(400,400)

obj = MyObject()
timer_id = obj.startTimer(100)

# obj.killTimer(timer_id)

window.show()

sys.exit(app.exec_())


