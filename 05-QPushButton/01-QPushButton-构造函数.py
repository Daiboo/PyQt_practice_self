import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QPushButton的创建")
window.resize(500,500)
window.move(400,250)


btn = QPushButton(QIcon("Icons/minus_48px.ico"),"这是一个按钮",window)  # 设置图标,文本,父控件
# btn.setParent(window)  # 手动设置父控件
# btn.setIcon()
# btn.setText()
# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())
