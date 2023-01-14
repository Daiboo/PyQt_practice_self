import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *


class Btn(QPushButton):
    """重写QPushButton,使得鼠标移动到上面即可展开菜单"""
    def enterEvent(self, a0: QtCore.QEvent) -> None:
        print("鼠标进入")
        self.showMenu()
        return super().enterEvent(a0)

class Menu(QMenu):        
    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.show()
        return super().enterEvent(a0)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        print("鼠标离开菜单",a0)
        self.close()
        return super().leaveEvent(a0)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QPushbutton-菜单")
window.resize(500, 500)
window.move(400, 250)

btn = Btn("按钮",window)

menu = Menu(btn)
# 子菜单 最近打开
# 行为动作:新建,打开 [分割线] 退出
new_action = QAction(QIcon("Icons/plus_48px.ico"),"新建",menu)  # 可以同时设置图标,文字,父对象
# new_action.setText("新建")
# new_action.setIcon(QIcon("Icons/plus_48px.ico"))
new_action.triggered.connect(lambda:print("新建文件"))  # new_action 的触发信号连接到槽函数


open_action = QAction(QIcon("Icons/search_48px.ico"),"打开",menu)
open_action.triggered.connect(lambda:print("打开文件"))

exit_action = QAction(QIcon("Icons/cross_48px.ico"),"关闭",menu)
exit_action.triggered.connect(lambda:qApp.exit())

open_recent_menu = Menu()
open_recent_menu.setTitle("最近打开")
# open_recent_menu.setIcon()
file_action = QAction("Python-Gui编程-PyQt5")
open_recent_menu.addAction(file_action)

menu.addAction(new_action)
menu.addAction(open_action)
menu.addMenu(open_recent_menu)  # 把一个menu放在另一个menu上,即成为子菜单  
menu.addSeparator()   # 添加分割线
menu.addAction(exit_action)

btn.setMenu(menu)


window.show()
sys.exit(app.exec_())




