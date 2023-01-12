from PyQt5.QtWidgets import QApplication,QWidget
import sys

# 要求： 每次改变窗口标题，都自动加上muzing前缀，能重复使用

app = QApplication(sys.argv)

window = QWidget()
window.resize(500,500)
window.move(400,250)


# 连接窗口标题变化的信号与槽

def cao(title):
    print("窗口标题变成了: " ,title)
    window.blockSignals(True)  # 避免出现死循环
    window.setWindowTitle("muzing"+title)
    window.blockSignals(False) # 回复连接，使下一次还能进行修改

window.windowTitleChanged.connect(cao)

window.setWindowTitle("信号的操作案例")
# window.setWindowTitle("修改后的标题")

window.show()

sys.exit(app.exec_())

