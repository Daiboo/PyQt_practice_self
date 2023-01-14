import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QWidget):
    def mousePressEvent(self, evt) -> None:
        # print(self.focusWidget())  
        # self.focusNextChild()  # 焦点切换到下一个子控件
        # self.focusPreviousChild()  # 焦点切换到上一个子控件
        pass

app = QApplication(sys.argv)

window = Window()

window.setWindowTitle("焦点控制")
window.resize(500,500)
window.move(400,250)

le1 = QLineEdit(window)
le1.move(50,50)

le2 = QLineEdit(window)
le2.move(50,100)

le3 = QLineEdit(window)
le3.move(50,150)

# 是一个静态方法，设置了子控件获取焦点的先后顺序
window.setTabOrder(le1,le3)  # 把window替换成QWidget也可以
window.setTabOrder(le3,le1)

le2.setFocus()  # 设置获取焦点
# le2.clearFocus()  # 清空获取焦点
# le2.setFocusPolicy(Qt.TabFocus)  # 设置获取焦点策略为仅通过Tab键获取
# le2.setFocusPolicy(Qt.ClickFocus)  # 设置获取焦点策略为仅通过鼠标点击获取
le2.setFocusPolicy(Qt.StrongFocus)  #  设置获取焦点策略为鼠标点击、Tab两种方式，也是默认值
# le2.setFocusPolicy(Qt.NoFocus)   # 设置不能通过两种方式获得焦点

window.show()
# 获取当前窗口内部，所有子控件当中获取焦点的那个控件
print(window.focusWidget())
sys.exit(app.exec_())


