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

window.setWindowTitle("QLineEdit-自定义行为")
window.resize(500, 500)
window.move(400, 250)

le = QLineEdit(window)
le.move(100,100)
action = QAction(le)  # 添加自定义行为
action.setToolTip("密码不可见")

def change():
    if le.echoMode() == QLineEdit.Password:
        le.setEchoMode(QLineEdit.Normal)
        action.setToolTip("密码可见")
        action.setIcon(QIcon("Icons/eye_48px.ico"))
    else:
        le.setEchoMode(QLineEdit.Password)
        action.setToolTip("密码不可见")
        action.setIcon(QIcon("Icons/eye_no.ico"))


action.setIcon(QIcon("Icons/eye_no.ico"))
action.triggered.connect(change)
le.addAction(action,QLineEdit.LeadingPosition)  # 在首部添加行为
le.addAction(action,QLineEdit.TrailingPosition)   # 在尾部添加行为
le.setEchoMode(QLineEdit.Password)


# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())

