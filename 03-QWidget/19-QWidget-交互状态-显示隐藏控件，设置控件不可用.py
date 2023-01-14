import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QWidget):
    def paintEvent(self,evt):
        print("窗口被绘制了")
        return super().paintEvent(evt)

class Btn(QPushButton):
    def paintEvent(self,evt):
        print("按钮被绘制了")
        return super().paintEvent(evt)

app = QApplication(sys.argv)

window = Window()

window.setWindowTitle("交互状态")
window.resize(500,500)
window.move(400,250)

btn  = Btn(window)
btn.setText("按钮")
# btn.pressed.connect(lambda:print("按钮被点击了"))
btn.pressed.connect(lambda:btn.setVisible(False))
# btn.setEnabled(False)  # 使按钮不可用
# btn.setVisible(False)  # 使按钮不可见

window.show()
# window.setVisible(True)  # show() 等方法都是setVisible方法的马甲
# window.setHidden(False)

print(btn.isHidden())   # 当window没有被绘制时，也是False
print(btn.isVisible())
print(btn.isVisibleTo(window))  # 父控件如果被显示时，子控件是否跟着被显示

sys.exit(app.exec_())


 