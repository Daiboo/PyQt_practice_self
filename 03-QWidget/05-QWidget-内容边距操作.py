import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel


app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("内容边距的设定")
window.resize(500,500)

label = QLabel(window)
label.setText("ABC")
label.resize(300,300)
label.setStyleSheet("background-color:cyan;font-size:30px")

label.setContentsMargins(150,0,0,0)

print(label.contentsRect())  # 内容矩形

window.show()

sys.exit(app.exec_())
