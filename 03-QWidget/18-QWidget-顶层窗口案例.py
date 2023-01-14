import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

"""案例:创建一个无边框,半透明的窗口;自定义关闭,最大化,最小化三个按钮;实现能够点击用户区域拖动窗口"""

class Window(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框窗口Flag
        self.setWindowOpacity(0.85)  # 设置不透明度
        self.setWindowTitle("顶层窗口操作-案例")
        self.setWindowIcon(QIcon("Icons/snowflake_128px.ico"))
        self.resize(500,500)
        print("第一次resize()")
        self.move(400,240)

        # 公共数据（通过保存为self的属性来实现跨方法使用）
        self.top_margin = 1  # 三个按钮距离顶部的距离
        self.btn_w = 32  # 按钮宽度
        self.btn_h = 32  # 按钮高度

        self.setup_ui()

    def setup_ui(self):
        """在窗口的右上角添加关闭,最大化,最小化 三个按钮.注意三个按钮的位置没有在本方法中确定,在resizeEvent中确定"""
        print("调用setup_ui")
        close_btn = QPushButton(self)
        self.close_btn = close_btn  # 通过把局部变量储存为对象属性来实现跨方法使用
        close_btn.setIcon(QIcon("Icons/cross_48px.ico"))
        # close_btn.setText("关闭")
        close_btn.resize(self.btn_w,self.btn_h)

        max_btn = QPushButton(self)
        self.max_btn = max_btn
        max_btn.setIcon(QIcon("Icons/expand_48px.ico"))
        # max_btn.setText("最大化")
        max_btn.resize(self.btn_w,self.btn_h)

        mini_btn = QPushButton(self)
        self.mini_btn = mini_btn  
        mini_btn.setIcon(QIcon("Icons/minus_48px.ico"))
        # mini_btn.setText("最小化")
        mini_btn.resize(self.btn_w,self.btn_h)


        # 监听按钮，连接信号与曹
        close_btn.pressed.connect(lambda:self.close())
        mini_btn.pressed.connect(lambda:self.showMinimized())

        def max_normal():
            """最大化/回复 按钮的槽函数"""
            if self.isMaximized():
                max_btn.setIcon(QIcon("Icons/expand_48px.ico"))   # 设置图标
                self.label.setText("hello world")
                self.label.setStyleSheet("font-size:30px;")
                self.label.adjustSize()
                self.showNormal()
            else:
                self.label.setText("Life is short,use python")
                self.label.setStyleSheet("font-size:40px")
                self.label.adjustSize()
                self.showMaximized()
                max_btn.setIcon(QIcon("Icons/contract_48px.ico"))
        


        max_btn.pressed.connect(max_normal)
        
        label = QLabel("hello world",self)
        self.label = label
        label.setStyleSheet("font-size:30px")
        label.adjustSize()
        print("label大小初始化")
        lab_x = int((self.width() - label.width()) / 2)   # label居中
        lab_y = int((self.height() - label.height()) / 2)  # label居中
        label.move(lab_x,lab_y)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        """当窗口大小改变时,重新移动三个按钮的位置"""
        print("resizeEvent发生")  # 结论:在程序的运行中会自动发生一次resizeEvent事件
        self.close_btn.move(self.width() - self.btn_w,self.top_margin)
        self.max_btn.move(self.width() - self.btn_w * 2,self.top_margin)
        self.mini_btn.move(self.width() - self.btn_w * 3,self.top_margin)
        self.label.move(
            int((self.width()-self.label.width())/2),
            int((self.height() - self.label.height())/2)
        )
        return super().resizeEvent(a0)

    def mousePressEvent(self,evt):
        if evt.button() == Qt.LeftButton:  # 尽在鼠标左键按下时拖动
            self.move_flag = True   # 设置一个标记，确保只有在执行 mousePressEvent之后才会执行 mouseMoveEvent
            # 确定两个点（鼠标第一次按下的点，窗口当前所在的原始点）
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            self.origen_x = self.x()
            self.origen_y = self.y()

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.move_flag:
            move_x = a0.globalX() - self.mouse_x
            move_y = a0.globalY() - self.mouse_y
            dest_x = self.origen_x + move_x
            dest_y = self.origen_y + move_y
            self.move(dest_x, dest_y)

        return super().mouseMoveEvent(a0)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.move_flag = False  # 鼠标释放后重置标记，避免无法拖动
        return super().mouseReleaseEvent(a0)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec_())




       


        



