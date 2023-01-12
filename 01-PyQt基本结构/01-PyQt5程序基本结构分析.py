import sys
from PyQt5.QtWidgets import QApplication,QWidget,qApp,QLabel

app = QApplication(sys.argv)
print(app.arguments())

print(qApp.arguments())  # 全局变量
# 上面两个都是一样的

window = QWidget()
window.setWindowTitle("这是一个窗口标题")
window.setGeometry(500,250,500,500)

# 控件也可以做欸一个容器(承载其他控件)
label = QLabel(window)  # 注意要写明父类
label.setText("label里的文字")
label.move(100,100)


window.show()


sys.exit(app.exec_())
