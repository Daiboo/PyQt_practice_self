import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("窗口移动的学习")
        self.resize(500,500)
        self.move(400,250)
        self.move_flag = False  # 设置一个标记，确保只有在执行mousePressEvent之后才会执行mouseMoveEvent
        self.setup_ui()

    def setup_ui(self):
        pass

    def mousePressEvent(self,evt):
        print("鼠标按下")

        if evt.button() == Qt.LeftButton:  # 尽在鼠标左键下时可以拖动
            self.move_flag = True  # 设置一个标记，确保只有在执行mousepressEvent之后才会执行mouseMoveEvent
            # 确保两个点（鼠标第一次按下的点，窗口当前所在的原始点）
            self.mouse_x = evt.globalX()  # 事件分相对和绝对坐标
            self.mouse_y = evt.globalY()
            print(self.mouse_x,self.mouse_y)
            self.origen_x = self.x()  
            self.origen_y = self.y()
            print(self.origen_x,self.origen_y)

    def mouseMoveEvent(self, evt: QtGui.QMouseEvent) -> None:
        if self.move_flag:
            print(evt.globalX(),evt.globalY())

            # 计算的是移动向量
            move_x = evt.globalX() - self.mouse_x   # 事件发生的点（即移动到的点）-第一次鼠标点击的点
            move_y = evt.globalY() - self.mouse_y
            dest_x = self.origen_x + move_x
            dest_y = self.origen_y + move_y
            self.move(dest_x,dest_y)
        return super().mouseMoveEvent(evt)

    # def mouseMoveEvent(self,evt) -> None:
    #     print("鼠标移动")
    #     if self.move_flag:
    #         print(evt.globalX(),evt.globalY())

    #         # 计算的是移动向量
    #         move_x = evt.globalX() - self.mouse_x   # 事件发生的点（即移动到的点）-第一次鼠标点击的点
    #         move_y = evt.globalY() - self.mouse_y
    #         dest_x = self.origen_x + move_x
    #         dest_y = self.origen_y + move_y
    #         self.move(dest_x,dest_y)

    def mouseReleaseEvent(self,a0:QtGui.QMouseEvent) ->None:
        self.move_flag = False  # 鼠标释放后重置标记，避免无法释放拖动
        print("鼠标释放")
        super().mouseReleaseEvent(a0)

app = QApplication(sys.argv)


window = Window()

window.setMouseTracking(True)   # 当开启鼠标跟踪后情况有所变化，所以才需要move_flag标记,
                                 # 原因出现在这里，开启鼠标追踪，实时产生鼠标移动事件，
                                 # 由于鼠标移动事件比鼠标按压事件先，所以才会出现：Window' object has no attribute 'move_flag

window.show()

sys.exit(app.exec_())




