from PyQt5.QtWidgets import QWidget,QApplication
import sys

class MyWindow(QWidget):
    def mouseMoveEvent(self,me):
        print("鼠标移动了",me.globalPos())  # 坐标值为相对整个电脑屏幕
        # print("鼠标移动了",me.localPos())  # 坐标值为相对本Widget窗口

app = QApplication(sys.argv)

window = MyWindow()

window.setWindowTitle("鼠标跟踪")
window.resize(500,500)
window.move(400,250)
window.setMouseTracking(True)  # 启动鼠标追踪，即使不按下鼠标左键，也时刻跟踪鼠标位置
print(window.hasMouseTracking())  # True

window.show()

sys.exit(app.exec_())



