from PyQt5.QtWidgets import QLabel,QApplication,QWidget
from PyQt5.QtCore import Qt
import sys

class  Mylabel(QLabel):
    def keyPressEvent(self,evt):    # 重写键盘按压事件
        if evt.key() == Qt.Key_Tab:
            self.setText("Tab键被点击了")
        # 注意Ctrl,Alt等修饰键的写法
        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            self.setText("Ctrl+S被点击了")
        
        # 多个修饰键之间用按位 或 来连接
        if(evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_S):
            self.setText("Ctrl + Shift + S 被点击了")

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("键盘点击案例")
window.resize(500,500)
window.move(400,250)

label = Mylabel(window)
label.resize(200,200)
label.move(140,120)
label.setStyleSheet("background-color:cyan;")
label.grabKeyboard()  # 开启抓取键盘操作

window.show()

sys.exit(app.exec_())

