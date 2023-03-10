import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QAbstractButton-模拟点击")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)
btn.setText("这是按钮1")
btn.pressed.connect(lambda: print("按钮1被点击"))

# btn.click()  # 模拟用户点击,不带动画
btn.animateClick(1000)  # 模拟持续按下1000m后在松开,代动画

btn2 = QPushButton(window)
btn2.setText("按钮2")
btn2.move(50,100)

def test():
    # btn.click()
    btn.animateClick(1000)  # 动画点击

btn2.pressed.connect(test)


window.show()

sys.exit(app.exec_())
