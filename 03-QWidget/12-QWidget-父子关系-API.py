from PyQt5.QtWidgets import QApplication,QLabel,QWidget
import sys

app = QApplication(sys.argv)

window  = QWidget()

window.setWindowTitle("父子关系的学习")

window.resize(500,500)

window.move(400,250)

label1 = QLabel(window)
label1.setText("标签1")
label1.move(0,20)

label2 = QLabel(window)
label2.setText("标签2")
label2.move(50,20)

label3 = QLabel(window)
label3.setText("标签3")
label3.move(100,20)

print(window.childAt(0,20))  # 根据指定父控件坐标点，找到对应的子空间
print(label2.parent())

print(window.childrenRect())  # 子空间组成的矩形区域   QRect(0, 20, 200, 30)

window.show()

sys.exit(app.exec_())

