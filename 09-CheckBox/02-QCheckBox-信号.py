import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QCheckBox-信号")
window.resize(500, 500)
window.move(400, 250)

cb = QCheckBox("Python",window)
cb.setIcon(QIcon("Icons/python_96px.ico"))
cb.setTristate(True)
cb.stateChanged.connect(lambda state: print(state))  # 1 2 0
# cb.toggled.connect(lambda isChecked: print(isChecked))  # True False


# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())