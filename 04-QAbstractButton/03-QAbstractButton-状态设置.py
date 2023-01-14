import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QAbstractButton-状态设置")
window.resize(500, 500)
window.move(400, 250)


btn = QPushButton(window)
btn.setIcon(QIcon("Icons/minus_48px.ico"))

push_button = QPushButton(window)
push_button.setText("这是QPushButton")
push_button.move(100, 100)
push_button.setStyleSheet(
    "QPushButton:pressed {background-color:red;}"
)  # # 通过QSS设置了按下时的样式

radio_button = QRadioButton(window)
radio_button.setText("这是RadioButton")
radio_button.move(100, 150)

check_box = QCheckBox(window)
check_box.setText("这是QCheckBox")
check_box.move(100, 200)

# 把三个按钮都置为按下状态
# push_button.setDown(True)
# radio_button.setDown(True)
# check_box.setDown(True)


push_button.setCheckable(True)  # 设置按钮为可选
print("push_button 是否能被选中：", push_button.isCheckable())
print("radio_button 是否能被选中：", radio_button.isCheckable())
print("check_box 是否能被选中：", check_box.isCheckable())

push_button.setChecked(True)  # 设置为被选
radio_button.setChecked(True)
check_box.setChecked(True)
print("push_button是否被选中了: ",push_button.isChecked())
print("radio_button是否被选中了：", radio_button.isChecked())
print("check_box是否被选中了：", check_box.isChecked())


def slot():
    """槽函数"""
    push_button.toggle()  # 交换 非选中/被选中状态
    radio_button.toggle()
    # check_box.toggle()
    check_box.setChecked(not check_box.isChecked())  # 等同于toggle()
    

btn.pressed.connect(slot)
check_box.setEnabled(False)  # 设置为不可选,但仍然可被btn的槽函数控制为被选中


 
window.show()

sys.exit(app.exec_())