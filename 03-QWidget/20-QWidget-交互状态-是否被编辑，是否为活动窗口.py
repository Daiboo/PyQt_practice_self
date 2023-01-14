import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("[*]交互状态")   # * 星号只有设置setWindowMofidied(True)才会被显示
window.resize(500,500)
window.move(400,250)

window.setWindowModified(True) 
print("窗口是否被编辑:" ,window.isWindowModified())

w2 = QWidget()  # 为验证活动窗口相关API而创建的另一个窗口
w2.show()

window.show()
w2.raise_()  # 即使提到前面，也不一定是活动窗口
# w2.setWindowState(Qt.WindowActive)  设置活动窗口

print("w2是否为活动窗口: ",w2.isActiveWindow())
print("window是否为活动窗口: " ,window.isActiveWindow())

sys.exit(app.exec_())

