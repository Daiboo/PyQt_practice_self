import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt


class Window(QWidget):
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        """点击用户区域,窗口在最大化最小化之间切换"""
        if self.isMaximized():  # 判断是否为最大窗口
            self.showNormal()
        else:
            self.showMaximized()

        return super().mousePressEvent(a0)

app = QApplication(sys.argv)

window = Window()

window.setWindowTitle("窗口最大化最小化")
window.resize(500,500)
window.move(400,250)


window.setWindowFlags(Qt.WindowStaysOnTopHint)  # 设置顶层窗口的Flag,窗口始终置于顶层
# window.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)  # 窗口无法调整大小
# window.setWindowFlags(Qt.FramelessWindowHint)  # 窗口无边框
# window.setWindowFlags(Qt.CustomizeWindowHint)  # 有边框但无标题栏和按钮，不能移动和拖动
# window.setWindowFlags(Qt.WindowTitleHint)    # 添加标题栏和一个不能使用enable(False)关闭按钮
# window.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint)  # 添加系统目录和一个关闭按钮
# window.setWindowFlags(Qt.WindowMinMaxButtonsHint)  # 激活最小化、最大化和不能使用的关闭按钮
# window.setWindowFlags(Qt.WindowMinimizeButtonHint)  # 激活最小化和禁用关闭按钮，禁用最大化按钮
# window.setWindowFlags(Qt.WindowMaximizeButtonHint)  # 激活最大化和禁用关闭按钮，禁用最小化按钮
# window.setWindowFlags(Qt.WindowCloseButtonHint)    # 添加一个关闭按钮
# window.setWindowFlags(Qt.WindowContextHelpButtonHint)  # 添加问号和禁用关闭按钮，同对话框
# window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)    # 窗口始终置于顶层并添加关闭按钮
# window.setWindowFlags(Qt.WindowStaysOnBottomHint)  # 窗口始终置于底层

window.show()

sys.exit(app.exec_())
