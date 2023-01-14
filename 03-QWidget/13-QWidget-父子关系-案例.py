import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

"""点击哪个label，哪个label的背景颜色就变红。重写QLabel和QWidget（父控件）两种方法"""

class MyLabel(QLabel):
    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.setStyleSheet("background-color:red;")
        print("被点击了",ev.localPos().x(),ev.y())  # 获取到的是事件相对label的坐标
        return super().mousePressEvent(ev)

class Window(QWidget):
    def mousePressEvent(self, evt: QtGui.QMouseEvent) -> None:
        if evt.button() == Qt.LeftButton:  # 只考虑按下左键的情况
            local_x = evt.x()   # 获取到的是相对Window坐标
            local_y = evt.y()
            sub_widget = self.childAt(local_x,local_y)
            if sub_widget is not None:
                sub_widget.setStyleSheet("background-color:red;")
            print("被点击了",local_x,local_y)
        return super().mousePressEvent(evt)

app = QApplication(sys.argv)

# window = Window()
window = QWidget()

window.setWindowTitle("父子关系案例")
window.resize(500,500)
window.move(400,250)

for i in range(1,11):
    label = MyLabel(window)
    label.setText(f"标签{i}")
    label.move(40*i,40*i)


window.show()
sys.exit(app.exec_())




