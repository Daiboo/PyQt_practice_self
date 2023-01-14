import sys

from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QAbstractButton 信号")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)
btn.setText("按钮1")
btn.move(200,200)
btn.setCheckable(True)

btn.pressed.connect(lambda: print("按钮被按下了"))
# btn.released.connect(lambda: print("按钮被释放了"))  # 控件内部松开鼠标,或者鼠标已出控件发送release信号
# btn.clicked.connect(lambda value:print("按钮被点击了",value))
# 只有控件有效范围内按下,在控件有效范围内松下,才发送信号;value值为按钮是否被选中
btn.toggled.connect(
    lambda value:print("按钮选中状态发生变化",value)
)
# print(btn.receivers(btn.pressed))
window.show()

sys.exit(app.exec_())


