import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)

window = QMainWindow()  #  QWidget 没有状态栏，故用QMainWindow
# 懒加载 —— 用到的时候，才会创建
window.statusBar()  # # 这里才加载出了状态栏

window.setWindowTitle("信息提示案例")
window.resize(500,500)
window.move(400,250)
window.setWindowFlags(Qt.WindowContextHelpButtonHint | Qt.WindowCloseButtonHint)  # 帮助菜单和关闭按钮
# 当把鼠标停留在控件身上之后，在状态栏提示一段文本
window.setToolTip("这是窗口")
window.setStatusTip("这是窗口")

label = QLabel(window)
label.setText("muzing")
label.setStatusTip("这是一个标签")   # 鼠标放在label上时，在状态栏出现的提示信息
label.setToolTip("这是一个提示标签")  # 鼠标放在并停留在label上时，出现的提示标签
# print(label.toolTip())
label.setToolTipDuration(2000)  # 设置提示标签出现的时长，单位为毫秒
# print(label.toolTipDuration())

label.setWhatsThis("这是啥?这是标签") # 切换到whatsThis模式下，点击label出现的说明信息

window.show()
sys.exit(app.exec_())


