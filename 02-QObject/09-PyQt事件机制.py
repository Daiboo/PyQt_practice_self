import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget
from PyQt5.QtCore import *
from PyQt5 import QtGui

class APP(QApplication):
    """重写QApplication类,捕捉并显示事件"""
    def notify(self,receiver,evt):
        if receiver.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(receiver,evt)
        return super().notify(receiver,evt)  # 负责分发
class Btn(QPushButton):
    def event(self,evt):
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)
        return super().event(evt)
    def mousePressEvent(self,*args,**kwargs)->None:
        print("鼠标被按下了...")
        return super().mousePressEvent(*args,**kwargs)

app = APP(sys.argv)

window = QWidget()
window.resize(500,500)

Btn = Btn(window)
Btn.setText("按钮")
Btn.move(200,200)

Btn.pressed.connect(lambda:print("cao-按钮被点击了"))

window.show()

sys.exit(app.exec_())

