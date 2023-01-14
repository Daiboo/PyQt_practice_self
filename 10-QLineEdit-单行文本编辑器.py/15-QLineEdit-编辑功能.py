import sys

from PyQt5.QtWidgets import *

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QLineEdit-编辑功能")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.move(100,100)
le.setDragEnabled(True)  # 设置为可以

